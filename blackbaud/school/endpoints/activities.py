from typing import Optional
from blackbaud.client import BaseSolutionClient


def get_activity_sections_by_level(
    school: BaseSolutionClient,
    level_id: int,
    school_year: Optional[str] = None,
):
    """
    Returns a collection of activity sections for the specified school level.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1ActivitiesSectionsGet
    """
    return school._make_request(
        "GET",
        "activities/sections",
        params={
            "level_num": level_id,
            "school_year": school_year,
        },
    )
