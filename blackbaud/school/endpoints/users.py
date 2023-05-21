from datetime import date, datetime
from decimal import Decimal
from typing import Iterable, Optional, TypedDict, Union

from requests import Response

from blackbaud.client import BaseSolutionClient


def get_user_by_id(
    school: BaseSolutionClient,
    user_id: int,
) -> Response:
    """
    Returns a user by ID.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idGet
    """
    return school._make_request("GET", f"users/{user_id}")


def get_users_by_roles(
    school: BaseSolutionClient,
    role_ids: Iterable[int],
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    email: Optional[str] = None,
    maiden_name: Optional[str] = None,
    grad_year: Optional[str] = None,
    end_grad_year: Optional[str] = None,
    marker: Optional[int] = None,
) -> Response:
    """
    Returns a paginated collection of users, limited to 100 users per page.
    https://developer.sky.blackbaud.com/docs/services/school/operations/v1usersget
    """
    return school._make_request(
        "GET",
        "users",
        params={
            "roles": ",".join(map(str, role_ids)),
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "maiden_name": maiden_name,
            "grad_year": grad_year,
            "end_grad_year": end_grad_year,
            "marker": marker,
        },
    )


def audit_users_by_role(
    school: BaseSolutionClient,
    role_id: int,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
) -> Response:
    """
    Returns a collection of audit information based on the specified role_id within the
    dates provided.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersAuditGet
    """
    return school._make_request(
        "GET",
        "users/audit",
        params={
            "role_id": role_id,
            "start_date": start_date.date().isoformat() if start_date else None,
            "end_date": end_date.date().isoformat() if end_date else None,
        },
    )


def get_changed_users_by_roles(
    school: BaseSolutionClient,
    role_ids: Iterable[int],
    start_date: Optional[datetime] = None,
) -> Response:
    """
    Returns a paginated collection of users whose data has been modified within the
    specified timeframe. The timeframe is from the start_date to the start_date plus
    seven days.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersChangedGet
    """
    return school._make_request(
        "GET",
        "users/changed",
        params={
            "base_role_ids": ",".join(map(str, role_ids)),
            "start_date": start_date.date().isoformat() if start_date else None,
        },
    )


def create_user(
    school: BaseSolutionClient,
    affiliation: Optional[str] = None,
    prefix: Optional[str] = None,
    first_name: Optional[str] = None,
    preferred_name: Optional[str] = None,
    middle_name: Optional[str] = None,
    last_name: Optional[str] = None,
    maiden_name: Optional[str] = None,
    suffix: Optional[str] = None,
    greeting: Optional[str] = None,
    gender: Optional[str] = None,
    birth_date: Optional[datetime] = None,
    deceased: Optional[bool] = None,
    email: Optional[str] = None,
    email_active: Optional[bool] = None,
    host_id: Optional[str] = None,
    lost: Optional[bool] = None,
    custom_field_one: Optional[str] = None,
    custom_field_two: Optional[str] = None,
    custom_field_three: Optional[str] = None,
    custom_field_four: Optional[str] = None,
    custom_field_five: Optional[str] = None,
    custom_field_six: Optional[str] = None,
    custom_field_seven: Optional[str] = None,
    custom_field_eight: Optional[str] = None,
    custom_field_nine: Optional[str] = None,
    custom_field_ten: Optional[str] = None,
) -> Response:
    """
    Creates a user. Returns the new user's User ID.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersPost
    """
    return school._make_request(
        "POST",
        "users",
        data={
            "affiliation": affiliation,
            "prefix": prefix,
            "first_name": first_name,
            "preferred_name": preferred_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "maiden_name": maiden_name,
            "suffix": suffix,
            "greeting": greeting,
            "gender": gender,
            "birth_date": birth_date.isoformat() if birth_date else None,
            "deceased": deceased,
            "email": email,
            "email_active": email_active,
            "host_id": host_id,
            "lost": lost,
            "custom_field_one": custom_field_one,
            "custom_field_two": custom_field_two,
            "custom_field_three": custom_field_three,
            "custom_field_four": custom_field_four,
            "custom_field_five": custom_field_five,
            "custom_field_six": custom_field_six,
            "custom_field_seven": custom_field_seven,
            "custom_field_eight": custom_field_eight,
            "custom_field_nine": custom_field_nine,
            "custom_field_ten": custom_field_ten,
        },
    )


def update_user(
    school: BaseSolutionClient,
    user_id: int,
    affiliation: Optional[str] = None,
    prefix: Optional[str] = None,
    first_name: Optional[str] = None,
    preferred_name: Optional[str] = None,
    middle_name: Optional[str] = None,
    last_name: Optional[str] = None,
    maiden_name: Optional[str] = None,
    suffix: Optional[str] = None,
    greeting: Optional[str] = None,
    gender: Optional[str] = None,
    birth_date: Optional[datetime] = None,
    deceased: Optional[bool] = None,
    email: Optional[str] = None,
    email_active: Optional[bool] = None,
    host_id: Optional[str] = None,
    lost: Optional[bool] = None,
    custom_field_one: Optional[str] = None,
    custom_field_two: Optional[str] = None,
    custom_field_three: Optional[str] = None,
    custom_field_four: Optional[str] = None,
    custom_field_five: Optional[str] = None,
    custom_field_six: Optional[str] = None,
    custom_field_seven: Optional[str] = None,
    custom_field_eight: Optional[str] = None,
    custom_field_nine: Optional[str] = None,
    custom_field_ten: Optional[str] = None,
) -> Response:
    """
    Updates a user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersPatch
    """
    return school._make_request(
        "PATCH",
        "users",
        data={
            "id": user_id,
            "affiliation": affiliation,
            "prefix": prefix,
            "first_name": first_name,
            "preferred_name": preferred_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "maiden_name": maiden_name,
            "suffix": suffix,
            "greeting": greeting,
            "gender": gender,
            "birth_date": birth_date.isoformat() if birth_date else None,
            "deceased": deceased,
            "email": email,
            "email_active": email_active,
            "host_id": host_id,
            "lost": lost,
            "custom_field_one": custom_field_one,
            "custom_field_two": custom_field_two,
            "custom_field_three": custom_field_three,
            "custom_field_four": custom_field_four,
            "custom_field_five": custom_field_five,
            "custom_field_six": custom_field_six,
            "custom_field_seven": custom_field_seven,
            "custom_field_eight": custom_field_eight,
            "custom_field_nine": custom_field_nine,
            "custom_field_ten": custom_field_ten,
        },
    )


def get_user_address_types(school: BaseSolutionClient) -> Response:
    """
    Returns a list of address types.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersAddresstypesGet
    """
    return school._make_request("GET", "users/addresstypes")


def create_user_address(
    school: BaseSolutionClient,
    user_id: int,
    address_type: int,
    country: str,
    line_one: str,
    line_two: Optional[str] = None,
    line_three: Optional[str] = None,
    city: Optional[str] = None,
    state: Optional[str] = None,
    postal_code: Optional[str] = None,
    province: Optional[str] = None,
    region: Optional[str] = None,
    is_mailing_address: Optional[bool] = None,
    is_primary_address: Optional[bool] = None,
) -> Response:
    """
    Creates an address for a user. Returns the ID of the address created.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idAddressesPost
    """
    return school._make_request(
        "POST",
        f"users/{user_id}/addresses",
        data={
            "user_id": user_id,
            "type_id": address_type,
            "country": country,
            "line_one": line_one,
            "line_two": line_two,
            "line_three": line_three,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "province": province,
            "region": region,
            "mailing_address": is_mailing_address,
            "primary": is_primary_address,
        },
    )


def update_user_address(
    school: BaseSolutionClient,
    user_id: int,
    address_id: int,
    address_type: Optional[int] = None,
    country: Optional[str] = None,
    line_one: Optional[str] = None,
    line_two: Optional[str] = None,
    line_three: Optional[str] = None,
    city: Optional[str] = None,
    state: Optional[str] = None,
    postal_code: Optional[str] = None,
    province: Optional[str] = None,
    region: Optional[str] = None,
    is_mailing_address: Optional[bool] = None,
    is_primary_address: Optional[bool] = None,
    links: Optional[Iterable[TypedDict]] = None,
) -> Response:
    """
    Updates an address for a user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idAddressesByAddress_idPatch
    """
    return school._make_request(
        "PATCH",
        f"users/{user_id}/addresses/{address_id}",
        data={
            "id": address_id,
            "user_id": user_id,
            "type_id": address_type,
            "country": country,
            "line_one": line_one,
            "line_two": line_two,
            "line_three": line_three,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "province": province,
            "region": region,
            "mailing_address": is_mailing_address,
            "primary": is_primary_address,
            "links": links,
        },
    )


def get_user_addresses(school: BaseSolutionClient, user_id: int) -> Response:
    """
    Returns a collection of addresses for a user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idAddressesGet
    """
    return school._make_request("GET", f"users/{user_id}/addresses")


def get_user_children(
    school: BaseSolutionClient,
    user_id: int,
) -> Response:
    """
    Returns a collection of children of the specified user_id.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByParent_idStudentsGet
    """
    return school._make_request("GET", f"users/{user_id}/students")


def get_custom_fields_by_roles(
    school: BaseSolutionClient,
    role_ids: Iterable[int],
    marker: Optional[int] = None,
    field_ids: Optional[Iterable[int]] = None,
) -> Response:
    """
    Returns a collection of custom fields for the specified roles.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersCustomfieldsByRolesGet
    """
    return school._make_request(
        "GET",
        "users/customfields",
        params={
            "base_role_ids": ",".join(map(str, role_ids)),
            "marker": marker,
            "field_ids": ",".join(map(str, field_ids)) if field_ids else None,
        },
    )


def get_user_custom_fields(
    school: BaseSolutionClient,
    user_id: int,
) -> Response:
    """
    Returns a collection of custom fields for a single user.
    Includes both user custom fields and administration view only custom fields.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idCustomfieldsGet
    """
    return school._make_request("GET", f"users/{user_id}/customfields")


def create_user_custom_field(
    school: BaseSolutionClient,
    user_id: int,
    field_id: int,
    data_type_id: int,
    value: Union[int, str, Decimal, datetime, date, bool],
) -> Response:
    """
    Creates an admin custom field for a user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idCustomfieldsPost
    """
    return school._make_request(
        "POST",
        f"users/{user_id}/customfields",
        data={
            "field_id": field_id,
            "data_type_id": data_type_id,
            "int_value": value if isinstance(value, int) else None,
            "text_value": value if isinstance(value, str) else None,
            "decimal_value": value if isinstance(value, Decimal) else None,
            "date_value": value.strftime("%Y/%m/%d")
            if isinstance(value, (datetime, date))
            else None,
            "bit_value": value if isinstance(value, bool) else None,
        },
    )


def update_user_custom_field(
    school: BaseSolutionClient,
    user_id: int,
    field_id: int,
    data_type_id: int,
    value: Union[int, str, Decimal, datetime, date, bool],
) -> Response:
    """
    Updates an admin custom field for a user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idCustomfieldsPatch
    """
    return school._make_request(
        "PATCH",
        f"users/{user_id}/customfields",
        data={
            "field_id": field_id,
            "data_type_id": data_type_id,
            "int_value": value if isinstance(value, int) else None,
            "text_value": value if isinstance(value, str) else None,
            "decimal_value": value if isinstance(value, Decimal) else None,
            "date_value": value.strftime("%Y/%m/%d")
            if isinstance(value, (datetime, date))
            else None,
            "bit_value": value if isinstance(value, bool) else None,
        },
    )
