import logging
from typing import List, Tuple
from models.Models import Assistance, Student
from gluon import current


class Repository:
  @staticmethod
  def add_student(student: Student) -> int:
    db = current.globalenv["db"]
    inserted_id = db.students.insert(
      name=student.name, grade=student.grade, age=student.age
    )
    return int(inserted_id)

  @staticmethod
  def get_subject_ids_by_grade(grade: int) -> List[int]:
    db = current.globalenv["db"]
    query = db.subjects.grade == grade
    student_ids = db(query).select(db.subjects.id)
    ids: List[int] = list(map(lambda row: int(row.id), student_ids))
    return ids

  @staticmethod
  def get_classroom_ids_and_dow_by_subject_id_on_schedules(id: int) -> List[Tuple[int, str]]:
    db = current.globalenv["db"]
    query = db.schedules.subject_id == id
    classroom_ids = db(query).select(db.schedules.classroom_id, db.schedules.day_of_week)
    ids: List[Tuple[int, str]] = list(map(lambda row: (int(row.classroom_id), str(row.day_of_week)), classroom_ids))
    return ids

  @staticmethod
  def get_student_ids_by_grade(grade: str) -> List[int]:
    db = current.globalenv["db"]
    query = db.students.grade == grade
    student_ids = db(query).select(db.students.id)
    ids: List[int] = list(map(lambda row: int(row.id), student_ids))
    return ids

  @staticmethod
  def get_grade_by_subject_id(id: int) -> str:
    db = current.globalenv["db"]
    query = db.subjects.id == id
    grade = db(query).select(db.subjects.grade)[0].grade
    logging.error(f"GRADE: {grade}")
    return str(grade)

  @staticmethod
  def add_assistance(assistance: Assistance) -> int:
    db = current.globalenv["db"]
    inserted_id = db.assistances.insert(
      student_id=assistance.student_id,
      subject_id=assistance.subject_id,
      classroom_id=assistance.classroom_id,
      week_number=assistance.week_number,
      day_of_week=assistance.day_of_week,
      assists=False,
    )
    return int(inserted_id)
