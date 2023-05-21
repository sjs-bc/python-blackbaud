from datetime import datetime
from typing import Optional

from requests import Response

from blackbaud.client import BaseSolutionClient


def get_attendance_records(
    school: BaseSolutionClient,
    level_id: int,
    date: datetime,
    offering_type: int,
    excuse_type: Optional[int] = None,
) -> Response:
    """
    Returns a collection of student attendance records for the specified day.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AttendanceGet
    """
    return school._make_request(
        "GET",
        "attendance",
        params={
            "level_id": level_id,
            "day": date.isoformat(),
            "offering_type": offering_type,
            "excuse_type": excuse_type,
        },
    )


def create_attendance_record(
    school: BaseSolutionClient,
    user_id: int,
    start_date: datetime,
    end_date: Optional[datetime] = None,
    specify_time: Optional[bool] = False,
    excuse_type: Optional[int] = None,
    excuse_comment: Optional[str] = None,
) -> Response:
    """
    Creates a new attendance record for the specified student.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AttendancePost
    """
    return school._make_request(
        "POST",
        "attendance",
        data={
            "student_user_id": user_id,
            "begin_date": start_date.isoformat(),
            "end_date": end_date.isoformat() if end_date else None,
            "start_time": start_date.time().isoformat("seconds")
            if specify_time
            else None,
            "end_time": end_date.time().isoformat("seconds")
            if (specify_time and end_date)
            else None,
            "excuse_type_id": excuse_type,
            "excuse_comment": excuse_comment,
        },
    )


def get_attendance_types(school: BaseSolutionClient) -> Response:
    """
    Returns a list of attendance types.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1TypesAttendancetypesGet
    """
    return school._make_request("GET", "types/attendancetypes")


def get_excuse_types(school: BaseSolutionClient) -> Response:
    """
    Returns a list of excuse types.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1TypesExcusedtypesGet
    """
    return school._make_request("GET", "types/excusedtypes")


def get_excuse_duration_types(school: BaseSolutionClient) -> Response:
    """
    Returns a list of excuse duration types.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1TypesExcusedurationtypesGet
    """
    return school._make_request("GET", "types/excusedurationtypes")
