from datetime import datetime
from typing import List, Optional, Literal
from blackbaud.client import BaseSolutionClient


def get_custom_fields(
    school: BaseSolutionClient,
):
    """
    Returns a collection of admin custom fields.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1CustomfieldsGet
    """
    return school._make_request("GET", "customfields")


def get_grade_levels(
    school: BaseSolutionClient,
):
    """
    Returns a collection of core school grade levels.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1gradelevelsget
    """
    return school._make_request("GET", "gradelevels")


def get_offering_types(
    school: BaseSolutionClient,
):
    """
    Returns a collection of core school offering types.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1offeringtypesget
    """
    return school._make_request("GET", "offeringtypes")


def get_roles(
    school: BaseSolutionClient,
):
    """
    Returns a collection of core school user roles.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1rolesget
    """
    return school._make_request("GET", "roles")


def get_school_levels(
    school: BaseSolutionClient,
):
    """
    Returns a collection of core school levels.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1levelsget
    """
    return school._make_request("GET", "levels")


def get_sessions(
    school: BaseSolutionClient,
    level_id: Optional[int] = None,
    school_year: Optional[str] = None,
):
    """
    Returns a collection of sessions for a higher education institution.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1SessionsGet
    """
    return school._make_request(
        "GET",
        "sessions",
        params={
            "level_num": level_id,
            "school_year": school_year,
        },
    )


def get_terms(
    school: BaseSolutionClient,
    school_year: Optional[str] = None,
    offering_type: Optional[int] = None,
):
    """
    Returns a collection of core school terms.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1termsget
    """
    return school._make_request(
        "GET",
        "sessions",
        params={
            "school_year": school_year,
            "offering_type": offering_type,
        },
    )


def get_timezone(
    school: BaseSolutionClient,
):
    """
    Returns the current time zone set for the school.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1TimezoneGet
    """
    return school._make_request("GET", "timezone")


def get_school_years(
    school: BaseSolutionClient,
):
    """
    Returns a collection of core school years.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1yearsget
    """
    return school._make_request("GET", "years")


def get_lists(
    school: BaseSolutionClient,
):
    """
    Returns a list of basic or advanced lists the authorized user has access to.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1ListsGet
    """
    return school._make_request("GET", "lists")


def get_list(
    school: BaseSolutionClient,
    list_id: int,
    page: Optional[int] = 1,
    page_size: Optional[int] = 1000,
):
    """
    Returns a collection of results from a basic or advanced list.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1ListsAdvancedByList_idGet
    """
    return school._make_request(
        "GET",
        f"lists/advanced/{list_id}",
        params={
            "page": page,
            "page_size": page_size,
        },
    )