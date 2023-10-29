from typing import Optional, List

from requests import Response

from blackbaud.client import BaseSolutionClient


def get_custom_fields(client: BaseSolutionClient, **request_kwargs) -> Response:
    """
    Returns a collection of admin custom fields.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1CustomfieldsGet
    """
    return client._make_request("GET", "customfields", **request_kwargs)


def get_grade_levels(client: BaseSolutionClient, **request_kwargs) -> Response:
    """
    Returns a collection of core school grade levels.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1gradelevelsget
    """
    return client._make_request("GET", "gradelevels", **request_kwargs)


def get_offering_types(client: BaseSolutionClient, **request_kwargs) -> Response:
    """
    Returns a collection of core school offering types.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1offeringtypesget
    """
    return client._make_request("GET", "offeringtypes", **request_kwargs)


def get_roles(client: BaseSolutionClient, **request_kwargs) -> Response:
    """
    Returns a collection of core school user roles.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1rolesget
    """
    return client._make_request("GET", "roles", **request_kwargs)


def get_school_levels(client: BaseSolutionClient, **request_kwargs) -> Response:
    """
    Returns a collection of core school levels.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1levelsget
    """
    return client._make_request("GET", "levels", **request_kwargs)


def get_sessions(
    client: BaseSolutionClient,
    school_level_id: Optional[int] = None,
    school_year: Optional[str] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of sessions for a higher education institution.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1SessionsGet
    """
    return client._make_request(
        "GET",
        "sessions",
        params={
            "level_num": school_level_id,
            "school_year": school_year,
        },
        **request_kwargs,
    )


def get_terms(
    client: BaseSolutionClient,
    school_year: Optional[str] = None,
    offering_type: Optional[int] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of core school terms.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1termsget
    """
    return client._make_request(
        "GET",
        "sessions",
        params={
            "school_year": school_year,
            "offering_type": offering_type,
        },
        **request_kwargs,
    )


def get_timezone(client: BaseSolutionClient, **request_kwargs) -> Response:
    """
    Returns the current time zone set for the client.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1TimezoneGet
    """
    return client._make_request("GET", "timezone", **request_kwargs)


def get_school_years(client: BaseSolutionClient, **request_kwargs) -> Response:
    """
    Returns a collection of core school years.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1yearsget
    """
    return client._make_request("GET", "years", **request_kwargs)


def get_lists(client: BaseSolutionClient, **request_kwargs) -> Response:
    """
    Returns a list of basic or advanced lists the authorized user has access to.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1ListsGet
    """
    return client._make_request("GET", "lists", **request_kwargs)


def get_list_page(
    client: BaseSolutionClient,
    list_id: int,
    page: int = 1,
    page_size: int = 1000,
    **request_kwargs,
) -> Response:
    """
    Returns a single page of results from a basic or advanced list.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1ListsAdvancedByList_idGet
    """
    return client._make_request(
        "GET",
        f"lists/advanced/{list_id}",
        params={
            "page": page,
            "page_size": page_size,
        },
        **request_kwargs,
    )


def get_list_page_contents(
    client: BaseSolutionClient,
    list_id: int,
    page: int = 1,
    page_size: int = 1000,
    **request_kwargs,
) -> dict:
    """
    get_list_page, but returns the contents of the page instead of the response object.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1ListsAdvancedByList_idGet
    """
    return get_list_page(client, list_id, page, page_size, **request_kwargs).json()


def get_full_list_contents(
    client: BaseSolutionClient,
    list_id: int,
    page: int = 1,
    page_size: int = 1000,
    **request_kwargs,
) -> dict:
    """
    Recursively fetches all results from a basic or advanced list.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1ListsAdvancedByList_idGet
    """
    full_list = {
        "count": 0,
        "results": {
            "rows": [],
        },
        "page": page,
    }

    while True:
        response = client._make_request(
            "GET",
            f"lists/advanced/{list_id}",
            params={
                "page": full_list["page"],
                "page_size": page_size,
            },
            **request_kwargs,
        )
        response_json = response.json()
        full_list["count"] += response_json["count"]
        full_list["results"]["rows"].extend(response_json["results"]["rows"])
        if response_json["count"] < page_size:
            break
        full_list["page"] += 1

    return full_list


def convert_advanced_list_to_dicts(advanced_list: dict) -> List[dict]:
    """
    Converts an advanced list response to a list of dictionaries.
    """
    return [
        {column["name"]: column.get("value", None) for column in row["columns"]}
        for row in advanced_list["results"]["rows"]
    ]


def get_directories(client: BaseSolutionClient, **request_kwargs) -> Response:
    """
    Returns a collection of directories the authorized user has access to.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1DirectoriesGet
    """
    return client._make_request("GET", "directories", **request_kwargs)


def search_directory(
    client: BaseSolutionClient,
    directory_id: int,
    search: str,
    search_all: Optional[bool] = True,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of results from a directory search.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1DirectoriesByDirectory_idSearchGet
    """
    return client._make_request(
        "GET",
        f"directories/{directory_id}",
        params={
            "search": search,
            "search_all": search_all,
        },
        **request_kwargs,
    )


def get_buildings(client: BaseSolutionClient, **request_kwargs) -> Response:
    """
    Returns a collection of school buildings.
    """
    return client._make_request("GET", "venues/buildings", **request_kwargs)
