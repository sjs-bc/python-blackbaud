from datetime import datetime
from typing import Iterable, Optional

from requests import Response

from blackbaud.client import BaseSolutionClient


def get_candidates(
    school: BaseSolutionClient,
    school_year: Optional[str] = None,
    status_ids: Optional[Iterable[int]] = None,
    modified_date: Optional[datetime] = None,
) -> Response:
    """
    Returns a collection of admissions candidates.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AdmissionsCandidatesGet
    """
    return school._make_request(
        "GET",
        "admissions/candidates",
        params={
            "school_year": school_year,
            "status_ids": ",".join(map(str, status_ids)),
            "modified_date": modified_date.isoformat(),
        },
    )


def get_checklist_statuses(
    school: BaseSolutionClient,
) -> Response:
    """
    Returns a collection of admissions checklist statuses.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AdmissionsCheckliststatusGet
    """
    return school._make_request("GET", "admissions/checkliststatus")


def get_checklists(
    school: BaseSolutionClient,
    search: Optional[str] = None,
    inactive_only: Optional[bool] = False,
) -> Response:
    """
    Returns a collection of admissions checklists.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AdmissionsChecklistsGet
    """
    return school._make_request(
        "GET",
        "admissions/checklists",
        params={
            "search_text": search,
            "inactive_only": inactive_only,
        },
    )


def get_admissions_statuses(
    school: BaseSolutionClient,
) -> Response:
    """
    Returns a collection of admissions statuses.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AdmissionsStatusGet
    """
    return school._make_request("GET", "admissions/status")
