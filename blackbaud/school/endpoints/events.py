from datetime import datetime
from typing import Optional

from requests import Response

from blackbaud.client import BaseSolutionClient


def get_calendar_for_self(
    client: BaseSolutionClient,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a list of events for the calling user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1EventsCalendarGet
    """
    return client._make_request(
        "GET",
        "events/calendar",
        params={
            "start_date": start_date.isoformat() if start_date else None,
            "end_date": end_date.isoformat() if end_date else None,
        },
        **request_kwargs,
    )


def get_categories(
    client: BaseSolutionClient,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of event categories.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1EventsCategoriesGet
    """
    return client._make_request("GET", "events/categories", **request_kwargs)
