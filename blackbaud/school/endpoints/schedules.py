from datetime import datetime
from typing import Literal, Optional

from requests import Response

from blackbaud.client import BaseSolutionClient


def get_athletics_schedules(
    client: BaseSolutionClient,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a list of schedules for the calling user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1SchedulesAthleticsGet
    """
    return client._make_request(
        "GET",
        "athletics/schedules",
        params={
            "start_date": start_date.isoformat() if start_date else None,
            "end_date": end_date.isoformat() if end_date else None,
        },
        **request_kwargs,
   )

def get_section_meetings(
    client: BaseSolutionClient,
    start_date: datetime,
    end_date: Optional[datetime] = None,
    offering_types: Optional[list[Literal[
        "academics", "activities", "advisory", "athletics"]]] = None,
    section_ids: Optional[list[int]] = None,
    last_modified: Optional[datetime] = None,
    show_time_for_current_date: Optional[bool] = None,
) -> Response:
    """
    Returns a list of section meetings for the calling user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1SchedulesMeetingsGet
    """
    return client._make_request(
        "GET",
        "schedules/section_meetings",
        params={
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat() if end_date else None,
            "offering_types": offering_types,
            "section_ids": section_ids,
            "last_modified": last_modified.isoformat() if last_modified else None,
            "show_time_for_current_date": show_time_for_current_date,
        },
    )