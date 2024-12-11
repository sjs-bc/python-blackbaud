from datetime import datetime
from typing import Iterable, Optional

from requests import Response

from blackbaud.client import BaseSolutionClient, paginated_response


def get_user_conditions(
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of medical conditions for a user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1MedicalUsersByUser_idConditionsGet
    """
    return client._make_request(
        "GET",
        f"medical/users/{user_id}/conditions",
        **request_kwargs,
    )

def get_user_allergies(
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of medical allergies for a user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1MedicalUsersByUser_idAllergiesGet
    """
    return client._make_request(
        "GET",
        f"medical/users/{user_id}/allergies",
        **request_kwargs,
    )

def get_user_medications(
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of medications for a user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1MedicalUsersByUser_idMedicationsGet
    """
    return client._make_request(
        "GET",
        f"medical/users/{user_id}/medications",
        **request_kwargs,
    )
