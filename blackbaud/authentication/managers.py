from oauthlib.oauth2 import OAuth2Token
from typing import Optional


class MemoryCredentialManager(object):
    """
    Default implementation of a credential manager, which stores
    credentials in memory.
    """

    def __init__(self):
        """
        Initialize with an empty token variable.
        """
        self._token = None

    def update_token(self, token: OAuth2Token) -> None:
        """
        Persist new credentials after a refresh.
        """
        self._token = token

    @property
    def token(self) -> Optional[OAuth2Token]:
        """
        Get the token. Should return None if no token is available.
        """
        return self._token
