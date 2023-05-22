from typing import Optional

from requests import Response

from blackbaud.client import BaseSolutionClient


def get_activity_sections_by_level(
    client: BaseSolutionClient,
    level_id: int,
    school_year: Optional[str] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of activity sections for the specified school level.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1ActivitiesSectionsGet
    """
    return client._make_request(
        "GET",
        "activities/sections",
        params={
            "level_num": level_id,
            "school_year": school_year,
        },
        **request_kwargs,
    )
