from datetime import datetime
from typing import Iterable, Optional, Literal
from blackbaud.client import BaseSolutionClient


def get_assignments_by_section(
    school: BaseSolutionClient,
    section_id: int,
    types: Optional[Iterable[str]] = None,
    status: Optional[str] = None,
    persona_id: Optional[Literal["2", 2, "3", 3]] = None,
    filter: Optional[Literal["expired", "future", "all"]] = "all",
    search: Optional[str] = None,
):
    """
    Gets a collection of assignments for a given section.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSectionsBySection_idAssignmentsGet
    """
    return school._make_request(
        "GET",
        f"academics/sections/{section_id}/assignments",
        params={
            "types": types,
            "status": status,
            "persona_id": persona_id,
            "filter": filter,
            "search": search,
        },
    )


def get_assignments_by_student(
    school: BaseSolutionClient,
    student_id: int,
    start_date: datetime,
    end_date: Optional[datetime] = None,
    section_ids: Optional[Iterable[int]] = None,
):
    """
    Gets a collection of assignments for a given student.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsByStudent_idAssignmentsGet
    """
    return school._make_request(
        "GET",
        f"academics/{student_id}/assignments",
        params={
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat() if end_date is not None else None,
            "section_ids": section_ids,
        },
    )


def get_courses(
    school: BaseSolutionClient,
    department_id: Optional[int] = None,
    level_id: Optional[int] = None,
):
    """
    Gets a collection of academic courses, filtered by department and/or school level.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsCoursesGet
    """
    return school._make_request(
        "GET",
        "academics/courses",
        params={
            "department_id": department_id,
            "level_id": level_id,
        },
    )


def get_cycles_by_section(
    school: BaseSolutionClient,
    section_id: int,
    duration_id: Optional[int] = None,
    group_type: Optional[int] = None,
):
    """
    Gets a collection of cycles for a given section.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSectionsBySection_idCyclesGet
    """
    return school._make_request(
        "GET",
        f"academics/sections/{section_id}/cycles",
        params={
            "duration_id": duration_id,
            "group_type": group_type,
        },
    )


def get_departments(
    school: BaseSolutionClient,
    level_id: Optional[int] = None,
):
    """
    Gets a collection of academic departments.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsDepartmentsGet
    """
    return school._make_request(
        "GET",
        "academics/departments",
        params={
            "level_id": level_id,
        },
    )


def enroll_students_into_sections(
    school: BaseSolutionClient,
    duration_id: int,
    enrollment_date: datetime,
    section_ids: Iterable[int],
    user_ids: Iterable[int],
):
    """
    Adds bulk enrollment data (students and/or teachers) for the specified section(s).
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSectionsStudentsPost
    """
    return school._make_request(
        "POST",
        "academics/sections/students",
        data={
            "id": duration_id,
            "enrollment_date": enrollment_date.isoformat(),
            "section_ids": ",".join(map(str, section_ids)),
            "user_ids": ",".join(map(str, user_ids)),
        },
    )


def get_graded_assignments_by_student(
    school: BaseSolutionClient,
    student_id: int,
    section_id: int,
    marking_period_id: int,
):
    """
    Returns the graded assignments for the specified student_id and their section_id.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsByStudent_idBySection_idGradedassignmentsGet
    """
    return school._make_request(
        "GET",
        f"academics/{student_id}/{section_id}/gradedassignments",
        params={
            "marking_period_id": marking_period_id,
        },
    )


def get_master_schedule(
    school: BaseSolutionClient,
    level_id: int,
    start_date: datetime,
    end_date: datetime,
    offering_type: Optional[int] = None,
):
    """
    Returns a collection of Master Schedule days within the date range provided.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSchedulesMasterGet
    """
    return school._make_request(
        "GET",
        "academics/schedules/master",
        params={
            "level_num": level_id,
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "offering_type": offering_type,
        },
    )


def get_schedule_set(school: BaseSolutionClient, schedule_set_id: int):
    """
    Returns details about the schedule set specified.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSchedulesSetsBySchedule_set_idGet
    """
    return school._make_request("GET", f"academics/schedules/sets/{schedule_set_id}")


def get_schedule_sets_by_level(
    school: BaseSolutionClient,
    level_id: int,
    school_year: Optional[str] = None,
    group_type: Optional[int] = None,
):
    """
    Returns a list of Schedule Sets for the specified school level.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSchedulesSetsGet
    """
    return school._make_request(
        "GET",
        "academics/schedules/sets",
        params={
            "level_num": level_id,
            "school_year": school_year,
            "group_type": group_type,
        },
    )


def get_sections_by_level(
    school: BaseSolutionClient,
    level_id: int,
    school_year: Optional[str] = None,
):
    """
    Returns a list of academic sections for the specified school level.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSectionsGet
    """
    return school._make_request(
        "GET",
        "academics/sections",
        params={"level_num": level_id, "school_year": school_year},
    )


def get_sections_by_teacher(
    school: BaseSolutionClient,
    teacher_id: int,
    school_year: Optional[str] = None,
):
    """
    Returns a list of sections for the specified teacher.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsTeachersByTeacher_idSectionsGet
    """
    return school._make_request(
        "GET",
        f"academics/teachers/{teacher_id}/sections",
        params={"school_year": school_year},
    )


def get_sections_by_student(
    school: BaseSolutionClient,
    student_id: int,
):
    """
    Returns a list of sections for the specified student.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsStudentByStudent_idSectionsGet
    """
    return school._make_request("GET", f"academics/student/{student_id}/sections")


def get_special_days(
    school: BaseSolutionClient,
    level_id: Optional[int] = None,
):
    """
    Returns a list of special days.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSpecialdaysGet
    """
    return school._make_request(
        "GET",
        "academics/specialdays",
        params={
            "level_id": level_id,
        },
    )


def get_enrollments_by_student(
    school: BaseSolutionClient,
    user_id: int,
    school_year: Optional[str] = None,
):
    """
    Returns a list of course sections in which the provided student is enrolled.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsEnrollmentsByUser_idGet
    """
    return school._make_request(
        "GET",
        f"academics/enrollments/{user_id}",
        params={
            "school_year": school_year,
        },
    )


def get_enrollment_changes(
    school: BaseSolutionClient,
    start_date: datetime,
    end_date: Optional[datetime] = None,
):
    """
    Returns a collection of students with enrollment changes on or after the date parameter.
    The maximum period of time that can be specified is 30 days from start_date, if end_date
    is not provided or is greater than 30 days from start_date it will be set to start_date + 30 days.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsEnrollmentsChangesGet
    """
    return school._make_request(
        "GET",
        "academics/enrollments/changes",
        params={
            "start_date": start_date,
            "end_date": end_date,
        },
    )


def get_students_by_section(
    school: BaseSolutionClient,
    section_id: int,
):
    """
    Returns the list of students in the specified section.
    https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSectionsBySection_idStudentsGet
    """
    return school._make_request("GET", f"academics/sections/{section_id}/students")
