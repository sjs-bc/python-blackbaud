from typing import Optional

from requests import Response

from blackbaud.client import BaseSolutionClient


def get_sections_by_level(
    school: BaseSolutionClient,
    level_id: int,
    school_year: Optional[str] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a list of advisory sections for the specified school level.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSectionsGet
    """
    return school._make_request(
        "GET",
        "advisories/sections",
        params={"level_num": level_id, "school_year": school_year},
        **request_kwargs,
    )
