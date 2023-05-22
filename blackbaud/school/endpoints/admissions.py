from datetime import datetime
from typing import Iterable, Optional

from requests import Response

from blackbaud.client import BaseSolutionClient


def get_candidates(
    client: BaseSolutionClient,
    school_year: Optional[str] = None,
    status_ids: Optional[Iterable[int]] = None,
    modified_date: Optional[datetime] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of admissions candidates.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AdmissionsCandidatesGet
    """
    return client._make_request(
        "GET",
        "admissions/candidates",
        params={
            "school_year": school_year,
            "status_ids": ",".join(map(str, status_ids)) if status_ids else None,
            "modified_date": modified_date.isoformat() if modified_date else None,
        },
        **request_kwargs,
    )


def get_checklist_statuses(
    client: BaseSolutionClient,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of admissions checklist statuses.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AdmissionsCheckliststatusGet
    """
    return client._make_request("GET", "admissions/checkliststatus", **request_kwargs)


def get_checklists(
    client: BaseSolutionClient,
    search: Optional[str] = None,
    inactive_only: Optional[bool] = False,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of admissions checklists.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AdmissionsChecklistsGet
    """
    return client._make_request(
        "GET",
        "admissions/checklists",
        params={
            "search_text": search,
            "inactive_only": inactive_only,
        },
        **request_kwargs,
    )


def get_admissions_statuses(
    client: BaseSolutionClient,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of admissions statuses.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AdmissionsStatusGet
    """
    return client._make_request("GET", "admissions/status", **request_kwargs)
