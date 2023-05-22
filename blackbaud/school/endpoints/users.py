from datetime import date, datetime
from enum import Enum
from decimal import Decimal
from typing import Iterable, Optional, TypedDict, Union

from requests import Response

from blackbaud.client import BaseSolutionClient


def get_self(
    client: BaseSolutionClient,
    **request_kwargs,
) -> Response:
    """
    Returns information about the caller.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersMeGet
    """
    return client._make_request("GET", "users/me", **request_kwargs)


def get_user_by_id(
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a user by ID.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idGet
    """
    return client._make_request("GET", f"users/{user_id}", **request_kwargs)


def get_user_by_id_details(
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a user by ID, with extended details.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersExtendedByUser_idGet
    """
    return client._make_request("GET", f"users/extended/{user_id}", **request_kwargs)


def get_users_by_roles(
    client: BaseSolutionClient,
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
    return client._make_request(
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


def get_users_by_roles_detailed(
    client: BaseSolutionClient,
    role_ids: Iterable[int],
    marker: Optional[int] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a paginated collection of extended user details, limited to 1000 users per
    page. Use the last user's ID as the marker value to return the next set of results.
    """
    return client._make_request(
        "GET",
        "users/extended",
        params={"base_role_ids": ",".join(map(str, role_ids)), "marker": marker},
        **request_kwargs,
    )


def audit_users_by_role(
    client: BaseSolutionClient,
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
    return client._make_request(
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
    client: BaseSolutionClient,
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
    return client._make_request(
        "GET",
        "users/changed",
        params={
            "base_role_ids": ",".join(map(str, role_ids)),
            "start_date": start_date.date().isoformat() if start_date else None,
        },
        **request_kwargs,
    )


def create_user(
    client: BaseSolutionClient,
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
    return client._make_request(
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
    client: BaseSolutionClient,
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
    return client._make_request(
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


def get_user_address_types(client: BaseSolutionClient, **request_kwargs) -> Response:
    """
    Returns a list of address types.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersAddresstypesGet
    """
    return client._make_request("GET", "users/addresstypes", **request_kwargs)


def create_user_address(
    client: BaseSolutionClient,
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
    return client._make_request(
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
    client: BaseSolutionClient,
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
    return client._make_request(
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
    client: BaseSolutionClient, user_id: int, **request_kwargs
) -> Response:
    """
    Returns a collection of addresses for a user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idAddressesGet
    """
    return client._make_request("GET", f"users/{user_id}/addresses", **request_kwargs)


def get_user_children(
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of children of the specified user_id.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByParent_idStudentsGet
    """
    return client._make_request("GET", f"users/{user_id}/students", **request_kwargs)


def get_custom_fields_by_roles(
    client: BaseSolutionClient,
    role_ids: Iterable[int],
    marker: Optional[int] = None,
    field_ids: Optional[Iterable[int]] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of custom fields for the specified roles.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersCustomfieldsByRolesGet
    """
    return client._make_request(
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
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of custom fields for a single user.
    Includes both user custom fields and administration view only custom fields.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idCustomfieldsGet
    """
    return client._make_request(
        "GET", f"users/{user_id}/customfields", **request_kwargs
    )


def create_user_custom_field(
    client: BaseSolutionClient,
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
    return client._make_request(
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
    client: BaseSolutionClient,
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
    return client._make_request(
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
    client: BaseSolutionClient,
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
    return client._make_request(
        "GET",
        "users/bbidstatus",
        params={
            "base_role_ids": ",".join(map(str, role_ids)),
            "marker": marker,
        },
        **request_kwargs,
    )


def get_user_education(
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of education information for the specified user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idEducationGet
    """
    return client._make_request("GET", f"users/{user_id}/education", **request_kwargs)


def get_changed_emergency_contacts(
    client: BaseSolutionClient,
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
    return client._make_request(
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
    client: BaseSolutionClient,
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
    return client._make_request(
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
    client: BaseSolutionClient,
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
    return client._make_request(
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
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of emergency contacts for the specified user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idEmergencycontactsGet
    """
    return client._make_request(
        "GET", f"users/{user_id}/emergencycontacts", **request_kwargs
    )


def get_user_employment(
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of employment details for the specified user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idEmploymentGet
    """
    return client._make_request("GET", f"users/{user_id}/employment", **request_kwargs)


def create_user_enrollment(
    client: BaseSolutionClient,
    user_id: int,
    grade_level_id: int,
    enrollment_date: datetime,
    school_level_id: Optional[int] = None,
    school_year: Optional[str] = None,
    departure_date: Optional[datetime] = None,
    current_year: Optional[bool] = None,
    has_grades: Optional[bool] = None,
    grade_repeated: Optional[bool] = None,
    graduated: Optional[bool] = None,
    allow_edit: Optional[bool] = None,
    allow_delete: Optional[bool] = None,
    future_enrollments: Optional[bool] = None,
    duration_id: Optional[int] = None,
    session_id: Optional[int] = None,
    role_ids: Optional[Iterable[int]] = None,
    **request_kwargs,
) -> Response:
    """
    TODO: Check if the optional parameters are actually optional
    Creates an enrollment for the given user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idEnrollmentsPost
    """
    return client._make_request(
        "POST",
        "users/enroll",
        data={
            "user_id": user_id,
            "grade_level_id": grade_level_id,
            "school_level_id": school_level_id,
            "school_year_label": school_year,
            "enroll_date": enrollment_date.date().isoformat()
            if enrollment_date
            else None,
            "depart_date": departure_date.date().isoformat()
            if departure_date
            else None,
            "current_year": current_year,
            "has_grades": has_grades,
            "grade_repeated": grade_repeated,
            "graduated": graduated,
            "allow_edit": allow_edit,
            "allow_delete": allow_delete,
            "future_enrollments": future_enrollments,
            "duration_id": duration_id,
            "session_id": session_id,
            "role_ids": role_ids,
        },
        **request_kwargs,
    )


def get_user_enrollments_by_year(
    client: BaseSolutionClient,
    school_year: str,
    school_level_id: Optional[int] = None,
    grade_level_id: Optional[int] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of enrollments for the specified user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idEnrollmentsGet
    """
    return client._make_request(
        "GET",
        "users/enrollments",
        params={
            "school_year": school_year,
            "school_level_id": school_level_id,
            "grade_level_id": grade_level_id,
            "limit": limit,
            "offset": offset,
        },
        **request_kwargs,
    )


def get_gender_types(
    client: BaseSolutionClient,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of gender types.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersGendertypesGet
    """
    return client._make_request("GET", "users/gendertypes", **request_kwargs)


def get_user_occupations(
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of occupations for the specified user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idOccupationsGet
    """
    return client._make_request("GET", f"users/{user_id}/occupations", **request_kwargs)


def create_user_occupation(
    client: BaseSolutionClient,
    user_id: int,
    business_name: Optional[str] = None,
    job_title: Optional[str] = None,
    business_url: Optional[str] = None,
    industry: Optional[str] = None,
    organization: Optional[str] = None,
    occupation: Optional[str] = None,
    matching_gift: Optional[bool] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    specialty: Optional[str] = None,
    parent_company: Optional[str] = None,
    job_function: Optional[str] = None,
    years_employed: Optional[int] = None,
    current: Optional[bool] = None,
    **request_kwargs,
) -> Response:
    """
    Creates an occupation for the given user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idOccupationsPost
    """
    return client._make_request(
        "POST",
        f"users/{user_id}/occupations",
        data={
            "business_name": business_name,
            "job_title": job_title,
            "business_url": business_url,
            "industry": industry,
            "organization": organization,
            "occupation": occupation,
            "matching_gift": matching_gift,
            "begin_date": start_date.date().isoformat() if start_date else None,
            "end_date": end_date.date().isoformat() if end_date else None,
            "specialty": specialty,
            "parent_company": parent_company,
            "job_function": job_function,
            "years_employed": years_employed,
            "current": current,
        },
        **request_kwargs,
    )


def get_phone_types(
    client: BaseSolutionClient,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of phone types.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersPhonetypesGet
    """
    return client._make_request("GET", "users/phonetypes", **request_kwargs)


def get_user_phones(
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of phones for the specified user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idPhonesGet
    """
    return client._make_request("GET", f"users/{user_id}/phones", **request_kwargs)


def create_user_phone(
    client: BaseSolutionClient,
    user_id: int,
    phone_type_id: int,
    phone_number: str,
    **request_kwargs,
) -> Response:
    """
    Creates a phone for the given user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idPhonesPost
    """
    return client._make_request(
        "POST",
        f"users/{user_id}/phones",
        data={
            "phone_type_id": phone_type_id,
            "phone_number": phone_number,
        },
        **request_kwargs,
    )


def get_user_relationships(
    client: BaseSolutionClient,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Returns a collection of relationships for the specified user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idRelationshipsGet
    """
    return client._make_request(
        "GET", f"users/{user_id}/relationships", **request_kwargs
    )


class RelationshipType(Enum):
    """
    Enum for relationship types.
    """

    NOT_SET = "NOT_SET"

    FRIEND = "Friend_Friend"
    ASSOCIATE = "Associate_Associate"
    CONSULTANT = "Consultant_Student"

    CUSTODIAN = "Custodian_Student"
    GUARDIAN = "Guardian_Ward"
    CARETAKER = "Caretaker_Charge"

    AUNT = "AuntUncle_NieceNephew"
    UNCLE = "AuntUncle_NieceNephew"
    COUSIN = "Cousin_Cousin"

    SPOUSE = "Spouse_Spouse"
    SPOUSE_PARTNER = "SpousePartner_SpousePartner"
    HUSBAND = "Husband_Wife"
    WIFE = "Husband_Wife"
    EX_SPOUSE = "ExHusband_ExWife"
    EX_HUSBAND = "ExHusband_ExWife"
    EX_WIFE = "ExHusband_ExWife"

    STEP_PARENT = "StepParent_StepChild"
    STEP_FATHER = "StepParent_StepChild"
    STEP_MOTHER = "StepParent_StepChild"
    STEP_SIBLING = "StepSibling_StepSibling"
    STEP_BROTHER = "StepSibling_StepSibling"
    STEP_SISTER = "StepSibling_StepSibling"
    HALF_SIBLING = "HalfSibling_HalfSibling"
    HALF_BROTHER = "HalfSibling_HalfSibling"
    HALF_SISTER = "HalfSibling_HalfSibling"

    GRANDPARENT = "Grandparent_Grandchild"
    GRANDFATHER = "Grandparent_Grandchild"
    GRANDMOTHER = "Grandparent_Grandchild"

    GREAT_GRANDPARENT = "GrGrandParent_GrGrandChild"
    GREAT_GRANDFATHER = "GrGrandParent_GrGrandChild"
    GREAT_GRANDMOTHER = "GrGrandParent_GrGrandChild"


def create_user_relationship(
    client: BaseSolutionClient,
    related_user_id: int,
    relationship_type: RelationshipType,
    user_id: int,
    list_as_parent: Optional[bool] = None,
    give_parental_access: Optional[bool] = None,
    tuition_responsible_signer: Optional[bool] = None,
    **request_kwargs,
) -> Response:
    """
    Creates a relationship record for the specified user.
    "[related_user_id] is a/the [relationship_type] of [user_id]"
    (ie. the related_user is on the LEFT side of the relationship)
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idRelationshipsPost
    """
    return client._make_request(
        "POST",
        f"users/{user_id}/relationships",
        data={
            "relationship_type": relationship_type.value,
            "give_parental_access": give_parental_access,
            "list_as_parent": list_as_parent,
            "tuition_responsible_signer": tuition_responsible_signer,
            "left_user": related_user_id,
        },
        **request_kwargs,
    )


def delete_user_relationship(
    client: BaseSolutionClient,
    related_user_id: int,
    relationship_type: RelationshipType,
    user_id: int,
    **request_kwargs,
) -> Response:
    """
    Deletes the specified relationship record for the specified user.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idRelationshipsByRelationship_idDelete
    """
    return client._make_request(
        "DELETE",
        f"users/{user_id}/relationships/",
        params={
            "left_user": related_user_id,
            "relationship_type": relationship_type.value,
        },
        **request_kwargs,
    )
