from abc import abstractmethod
from typing import Protocol, Optional
from oauthlib.oauth2 import OAuth2Token


class CredentialManager(Protocol):
    """
    A protocol for credential managers.

    A credential manager is responsible for persisting tokens.
    This could involve a file, a database, or just a variable in memory.

    """

    @abstractmethod
    def update_token(self, token: OAuth2Token) -> None:
        """
        A method that persists new credentials after a refresh.
        """
        ...

    @property
    def token(self) -> Optional[OAuth2Token]:
        """
        Get the token.
        """
        ...
