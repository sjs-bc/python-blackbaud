import logging
from datetime import datetime, timedelta
from typing import Any, Iterable, Literal, Optional, Type, Union

import requests
from limits import RateLimitItem
from limits.strategies import MovingWindowRateLimiter, RateLimiter
from requests_cache.backends import BackendSpecifier

from blackbaud.authentication.managers import MemoryCredentialManager
from blackbaud.authentication.protocols import CredentialManager
from blackbaud.authentication.settings import AUTHORIZATION_URL, TOKEN_URL
from blackbaud.client.rate_limiters.default import DEFAULT_STORAGE, STANDARD_TIER
from blackbaud.client.session import CachedOAuth2Session
from blackbaud.client.settings import BASE_URL

_logger = logging.getLogger(__name__)


class SKYAPIClient:
    """
    A client for the SKY API.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        subscription_key: str,
        redirect_uri: str,
        credential_manager: CredentialManager = MemoryCredentialManager(),
        state: Optional[str] = None,
        environment_id: Optional[str] = None,
        scope: Optional[str] = None,
        authorization_code: Optional[str] = None,
        authorization_response: Optional[str] = None,
        logger: Optional[logging.Logger] = _logger,
        rate_limiter: RateLimiter = MovingWindowRateLimiter(storage=DEFAULT_STORAGE),
        rate_limits: Iterable[RateLimitItem] = STANDARD_TIER,
        cache_name: str = "blackbaud_cache",
        cache_backend: Optional[BackendSpecifier] = None,
        cache_default_expiry: Union[int, float, str, datetime, timedelta] = timedelta(
            hours=1
        ),
    ):
        """
        Construct a new SKY API Client object.

        :param client_id: The client ID for your application.
        :type client_id: str
        :param client_secret: The client secret for your application.
        :type client_secret: str
        :param subscription_key: The Blackbaud subscription key for your application.
        :param redirect_uri: A valid redirect URI for your application.
        :type redirect_uri: str
        :param credential_manager: A credential manager object.
        :param state: A state string to be used in the OAuth flow.
        :type state: str, optional
        :param environment_id: The environment ID for your application. Provides a
        hint to the authorization page to filter the list of eligible environments
        shown to the specified value. Typically, this parameter will be used in
        conjunction with SKY Add-ins operating in the context of a host application
        to limit the scope of consent to the current environment.
        :type environment_id: str, optional
        :param scope: A space-separated list of scopes to request.
        :type scope: str, optional
        :param authorization_code: An authorization code to use in the OAuth flow. This
        can be used to skip the authorization step.
        :type authorization_code: str, optional
        :param authorization_response: A post-authorization redirect URL containing
        the authorization code. This can be used to skip the authorization step.
        :type authorization_response: str, optional

        """
        self._client_id = client_id
        self._client_secret = client_secret
        self._subscription_key = subscription_key
        self._redirect_uri = redirect_uri
        self._credential_manager = credential_manager
        self._state = state
        self._environment_id = environment_id
        self._scope = scope
        self.logger = logger
        self._rate_limiter = rate_limiter
        self._rate_limits = rate_limits

        self._session = CachedOAuth2Session(
            client_id=self._client_id,
            redirect_uri=self._redirect_uri,
            token=self._credential_manager.token,
            state=self._state,
            auto_refresh_url=TOKEN_URL,
            auto_refresh_kwargs={
                "client_id": self._client_id,
                "client_secret": self._client_secret,
            },
            token_updater=self._credential_manager.update_token,
            cache_name=cache_name,
            backend=cache_backend,
            expire_after=cache_default_expiry,
        )
        self._state = str(self._session.new_state())
        self._authorization_url, _ = self._session.authorization_url(
            AUTHORIZATION_URL,
            state=self._state,
            environment_id=self._environment_id,
        )
        if self._credential_manager.token is not None:
            self._credential_manager.update_token(
                self._session.refresh_token(
                    token_url=TOKEN_URL,
                    refresh_token=self._credential_manager.token["refresh_token"],
                )
            )
        elif authorization_code or authorization_response:
            self._credential_manager.update_token(
                self._session.fetch_token(
                    TOKEN_URL,
                    code=authorization_code,
                    authorization_response=authorization_response,
                    client_secret=self._client_secret,
                )
            )

    def fetch_token(
        self, code: Optional[str] = None, authorization_response: Optional[str] = None
    ) -> None:
        """
        Fetch a token using an authorization code or authorization response, and
        persist the token using the credential manager.

        :param code: The authorization code.
        :type code: str
        """
        if code is None and authorization_response is None:
            raise ValueError("Either a code or an authorization response is required.")

        token = self._session.fetch_token(
            TOKEN_URL,
            code=code,
            authorization_response=authorization_response,
            client_secret=self._client_secret,
        )
        self._credential_manager.update_token(token)

    def request(
        self,
        method: str,
        url: str,
        data: Optional[dict] = None,
        headers: Optional[dict] = None,
        withhold_token: bool = False,
        **kwargs,
    ) -> requests.Response:
        """
        Make an authenticated request to the SKY API.

        :param method: The HTTP verb to use.
        :type method: str
        :param url: The URL to request.
        :type url: str
        :param data: The data to send with the request.
        :type data: dict, optional
        :param headers: The headers to send with the request.
        :type headers: dict, optional
        :return: The response from the SKY API.
        :rtype: dict
        """
        if headers is None:
            headers = {}

        headers.update(
            {
                "Bb-Api-Subscription-Key": self._subscription_key,
                "Content-Type": "application/json",
            }
        )

        # if this request is not cached, then we need to rate limit it
        if not self._session.cache.contains(
            request=requests.Request(method, url, headers=headers, data=data)
        ):
            for limit in self._rate_limits:
                self._rate_limiter.hit(limit, self._subscription_key)

        return self._session.request(
            method,
            url,
            headers=headers,
            data=data,
            withhold_token=withhold_token,
            **kwargs,
        )

    @property
    def authorization_url(self) -> str:
        """
        Return the authorization URL.

        :return: The authorization URL.
        :rtype: str
        """
        return self._authorization_url

    @property
    def state(self) -> Optional[str]:
        """
        Return the state string.

        :return: The state string.
        :rtype: str
        """
        return self._state

    @property
    def environment_id(self) -> Optional[str]:
        """
        Return the environment ID.

        :return: The environment ID.
        :rtype: str
        """
        return self._environment_id


class Endpoint:
    """
    A base class for SKY API Endpoints
    """

    def __init__(self, client: Type["BaseSolutionClient"], data: dict):
        """
        Construct a new SKYEntity object.

        :param client: The SKY API client to use.
        :type client: SKYAPIClient
        :param data: The data for the entity.
        :type data: dict
        """
        self._client = client
        self._data = data


class BaseSolutionClient:
    """
    A base class for solution-specific clients.
    """

    def __init__(self, client: SKYAPIClient, slug: str, api_version: str):
        """
        Construct a new BaseSolutionClient object.

        :param client: The SKY API client to use.
        :type client: SKYAPIClient
        :param slug: The solution slug.
        :type slug: str
        :param api_version: The API version.
        :type api_version: str
        """
        self._client = client
        self._slug = slug
        self._api_version = api_version

    def __make_url(self, path: str) -> str:
        """
        Get the full URL for a given path in this solution.

        :param path: The path to the resource.
        :type path: str
        :return: The URL for the resource.
        :rtype: str
        """
        return f"{BASE_URL}/{self._slug}/{self._api_version}/{path}"

    def _make_request(
        self,
        http_verb: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
        path: str,
        data: Optional[dict[Any, Any]] = None,
        **kwargs,
    ) -> requests.Response:
        """
        Make a request to the SKY API.

        :param path: The path to the resource.
        :type path: str
        :return: The response from the SKY API.
        :rtype: dict
        """
        response = self._client.request(
            http_verb, self.__make_url(path), data=data, **kwargs
        )

        return response


def paginated_response(func):
    """
    A decorator for paginated responses.
    Given a function that returns a requests.Response object, this decorator will
    automatically handle pagination and return the full response as a dict.
    """

    def wrapper(*args, **kwargs) -> requests.Response:
        if not isinstance(args[0], BaseSolutionClient):
            raise TypeError(
                "The paginated_response decorator can only be used on methods "
                "that take a BaseSolutionClient as the first argument."
            )
        initial_response = func(*args, **kwargs)
        initial_response.raise_for_status()
        initial_response.full_json = initial_response.json()
        initial_response.pages = [initial_response.full_json]

        while initial_response.full_json.get("next_link"):
            subsequent_response = (
                args[0]
                ._make_request("GET", initial_response.full_json["next_link"])
            )
            subsequent_response.raise_for_status()
            initial_response.pages.append(subsequent_response.json())
            initial_response.full_json["value"].extend(subsequent_response["value"])
            initial_response.full_json["next_link"] = subsequent_response.get(
                "next_link"
            )

        initial_response.full_json["count"] = len(initial_response.full_json["value"])

        return initial_response

    return wrapper
