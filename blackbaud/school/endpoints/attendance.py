from datetime import datetime
from typing import Optional
from blackbaud.client import BaseSolutionClient


def get_attendance_records(
    school: BaseSolutionClient,
    level_id: int,
    date: datetime,
    offering_type: int,
    excuse_type: Optional[int] = None,
):
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
):
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
            "end_date": end_date.isoformat(),
            "start_time": start_date.time().isoformat("seconds")
            if specify_time
            else None,
            "end_time": end_date.time().isoformat("seconds") if specify_time else None,
            "excuse_type_id": excuse_type,
            "excuse_comment": excuse_comment,
        },
    )
