from datetime import date, datetime
from enum import Enum
from decimal import Decimal
from typing import Iterable, Optional, TypedDict, Union

from requests import Response

from blackbaud.client import BaseSolutionClient


def get_user_by_id(
    school: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a user by ID.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idGet
    """
    return school._make_request("GET", f"users/{user_id}", **request_kwargs)


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
    **request_kwargs,
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
        **request_kwargs,
    )


def audit_users_by_role(
    school: BaseSolutionClient,
    role_id: int,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    **request_kwargs,
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
        **request_kwargs,
    )


def get_changed_users_by_roles(
    school: BaseSolutionClient,
    role_ids: Iterable[int],
    start_date: Optional[datetime] = None,
    **request_kwargs,
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
        **request_kwargs,
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
    **request_kwargs,
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
        **request_kwargs,
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
    **request_kwargs,
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
        **request_kwargs,
    )


def get_user_address_types(school: BaseSolutionClient, **request_kwargs) -> Response:
    """
    Returns a list of address types.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersAddresstypesGet
    """
    return school._make_request("GET", "users/addresstypes", **request_kwargs)


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
    **request_kwargs,
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
        **request_kwargs,
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
    **request_kwargs,
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
        **request_kwargs,
    )


def get_user_addresses(
    school: BaseSolutionClient, user_id: int, **request_kwargs
) -> Response:
    """
    Returns a collection of addresses for a user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idAddressesGet
    """
    return school._make_request("GET", f"users/{user_id}/addresses", **request_kwargs)


def get_user_children(
    school: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of children of the specified user_id.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByParent_idStudentsGet
    """
    return school._make_request("GET", f"users/{user_id}/students", **request_kwargs)


def get_custom_fields_by_roles(
    school: BaseSolutionClient,
    role_ids: Iterable[int],
    marker: Optional[int] = None,
    field_ids: Optional[Iterable[int]] = None,
    **request_kwargs,
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
        **request_kwargs,
    )


def get_user_custom_fields(
    school: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of custom fields for a single user.
    Includes both user custom fields and administration view only custom fields.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idCustomfieldsGet
    """
    return school._make_request(
        "GET", f"users/{user_id}/customfields", **request_kwargs
    )


def create_user_custom_field(
    school: BaseSolutionClient,
    user_id: int,
    field_id: int,
    data_type_id: int,
    value: Union[int, str, Decimal, datetime, date, bool],
    **request_kwargs,
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
        **request_kwargs,
    )


def update_user_custom_field(
    school: BaseSolutionClient,
    user_id: int,
    field_id: int,
    data_type_id: int,
    value: Union[int, str, Decimal, datetime, date, bool],
    **request_kwargs,
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
        **request_kwargs,
    )


def get_user_bbid_status(
    school: BaseSolutionClient,
    role_ids: Iterable[int],
    marker: Optional[int] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a paginated collection of users education management BBID status,
    limited to 1000 users per page. Use the last user's ID as the marker value
    to return the next set of results.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersBbidstatusGet
    """
    return school._make_request(
        "GET",
        "users/bbidstatus",
        params={
            "base_role_ids": ",".join(map(str, role_ids)),
            "marker": marker,
        },
        **request_kwargs,
    )


def get_user_education(
    school: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of education information for the specified user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idEducationGet
    """
    return school._make_request("GET", f"users/{user_id}/education", **request_kwargs)


def get_changed_emergency_contacts(
    school: BaseSolutionClient,
    start_date: Optional[datetime] = None,
    marker: Optional[int] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a paginated collection of all emergency contacts for all users that have
    had changes since the specified start_date. If no date is specified then this
    returns a paginated collection of all emergency contacts for all users.
    Use the last user's ID as the marker value to return the next set of results.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersEmergencycontactsChangedGet
    """
    return school._make_request(
        "GET",
        "users/emergencycontacts/changed",
        params={
            "start_date": start_date.date().isoformat() if start_date else None,
            "marker": marker,
        },
        **request_kwargs,
    )


class AutomatedEmergencyContact(Enum):
    NEVER = 0
    EVERY_TIME = 1
    EMERGENCY_ONLY = 2


def create_emergency_contact(
    school: BaseSolutionClient,
    user_id: int,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    relationship: Optional[str] = None,
    phone_number: Optional[str] = None,
    phone_type: Optional[str] = None,
    automated_call: Optional[AutomatedEmergencyContact] = None,
    email: Optional[str] = None,
    automated_email: Optional[AutomatedEmergencyContact] = None,
    **request_kwargs,
):
    """
    Creates a non-user emergency contact for the given user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idEmergencycontactsNonuserPost
    """
    return school._make_request(
        "POST",
        f"users/{user_id}/emergencycontacts/nonuser",
        data={
            "automated_email": automated_email.value if automated_email else None,
            "email": email,
            "call_dialer": automated_call.value if automated_call else None,
            "firstname": first_name,
            "lastname": last_name,
            "phone_number": phone_number,
            "phone_type": phone_type,
            "relationship": relationship,
        },
        **request_kwargs,
    )


def create_emergency_contact_user(
    school: BaseSolutionClient,
    user_id: int,
    phone_number: Optional[str] = None,
    automated_call: Optional[AutomatedEmergencyContact] = None,
    email: Optional[str] = None,
    automated_email: Optional[AutomatedEmergencyContact] = None,
    **request_kwargs,
):
    """
    Creates a non-user emergency contact for the given user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idEmergencycontactsNonuserPost
    """
    return school._make_request(
        "POST",
        f"users/{user_id}/emergencycontacts/nonuser",
        data={
            "automated_email": automated_email.value if automated_email else None,
            "call_dialer": automated_call.value if automated_call else None,
            "email": email,
            "phone_number": phone_number,
        },
        **request_kwargs,
    )


def get_user_emergency_contacts(
    school: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of emergency contacts for the specified user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idEmergencycontactsGet
    """
    return school._make_request("GET", f"users/{user_id}/emergencycontacts", **request_kwargs)


def get_user_employment(
    school: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of employment details for the specified user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idEmploymentGet
    """
    return school._make_request("GET", f"users/{user_id}/employment", **request_kwargs)
