from datetime import datetime
from typing import Optional
from blackbaud.client import BaseSolutionClient


def get_calendar_for_self(
    school: BaseSolutionClient,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
):
    """
    Returns a list of events for the calling user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1EventsCalendarGet
    """
    return school._make_request(
        "GET",
        "events/calendar",
        params={
            "start_date": start_date.isoformat() if start_date is not None else None,
            "end_date": end_date.isoformat() if end_date is not None else None,
        },
    )


def get_categories(
    school: BaseSolutionClient,
):
    """
    Returns a collection of event categories.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1EventsCategoriesGet
    """
    return school._make_request("GET", "events/categories")
