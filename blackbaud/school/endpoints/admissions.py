from datetime import datetime
from typing import List, Optional, Literal
from blackbaud.client import BaseSolutionClient

def get_candidates(
    school: BaseSolutionClient,
    school_year: Optional[str] = None,
    status_ids: Optional[List[int]] = None,
    modified_date: Optional[datetime] = None,
    
):
    """
    Returns a collection of admissions candidates.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AdmissionsCandidatesGet
    """
    return school._make_request(
        "GET",
        "activities/sections",
        params={
            "school_year": school_year,
            "status_ids": ",".join(map(str, status_ids)),
            "modified_date": modified_date.isoformat(),
        },
    )