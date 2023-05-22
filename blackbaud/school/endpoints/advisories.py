from typing import Optional

from requests import Response

from blackbaud.client import BaseSolutionClient


def get_sections_by_level(
    client: BaseSolutionClient,
    school_level_id: int,
    school_year: Optional[str] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a list of advisory sections for the specified school level.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSectionsGet
    """
    return client._make_request(
        "GET",
        "advisories/sections",
        params={"level_num": school_level_id, "school_year": school_year},
        **request_kwargs,
    )
