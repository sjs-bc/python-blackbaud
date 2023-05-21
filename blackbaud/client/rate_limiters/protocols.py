from abc import abstractmethod
from typing import Any, Protocol


class RateLimiter(Protocol):
    """
    A protocol for rate limiter adapters. Based entirely on the
    `limits library <https://github.com/alisaifee/limits>`, as that's the library we
    will be using, but having this protocol allows anyone to swap it out for another
    library.
    """

    @abstractmethod
    def __init__(self, subscription_key: str, rate_limit: Any):
        """
        Construct a new RateLimiter object with the Blackbaud subscription key,
        through which Blackbaud evaluates rate limits.

        See: https://developer.blackbaud.com/skyapi/docs/basics#rate-limits
             https://developer.blackbaud.com/skyapi/docs/basics#quotas


        :param subscription_key: The Blackbaud subscription key.
        :type subscription_key: str
        :param rate_limit: Some description of the rate limit which will be interpreted
        by the implementation of the class to send out or delay requests.
        :type rate_limit: Any
        """
        ...

    @abstractmethod
    def hit(self, cost: int = 1) -> None:
        """
        Hit the rate limiter with a request, using up the number of requests
        specified in .

        :param cost: The cost of the request.
        :type cost: int
        """
        ...

    @abstractmethod
    def test(self, cost: int = 1) -> bool:
        """
        Test the rate limiter with a request.

        :param cost: The cost of the request.
        :type cost: int
        """
        ...
