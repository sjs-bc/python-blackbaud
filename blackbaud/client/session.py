from requests_oauthlib import OAuth2Session
from requests_cache import CacheMixin


class CachedOAuth2Session(CacheMixin, OAuth2Session):
    """
    OAuth2Session class with caching behavior.
    Accepts arguments for OAuth2Session and CachedSession.
    """
