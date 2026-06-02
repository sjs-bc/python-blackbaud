class CredentialsNotRefreshableError(Exception):
    """
    Exception raised when a refresh token is not available to refresh credentials.
    """
    pass


class AuthenticationError(Exception):
    """
    Exception raised when credentials that are expected to be valid cannot be
    authenticated. Also raised when credentials that are supposed to be
    refreshable cannot be refreshed.
    """
    pass
