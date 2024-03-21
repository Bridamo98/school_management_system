import logging

from repository.Repository import Repository
from factory.Factory import Factory


class BusinessLogic:
  @staticmethod
  def synchronize_assistances_from_schedules(form):
    subject_id = int(form.vars.subject_id)
    classroom_id = int(form.vars.classroom_id)
    day_of_week = str(form.vars.day_of_week)
    subject_grade = Repository.get_grade_by_subject_id(subject_id)
    logging.error(f"subject_grade: {subject_grade}")
    students_ids = Repository.get_student_ids_by_grade(subject_grade)
    logging.error(f"students_ids: {students_ids}")
    for student_id in students_ids:
      for week in range(1, 53):
        assistance = Factory.create_assistance(
          student_id=student_id,
          subject_id=subject_id,
          classroom_id=classroom_id,
          week_number=week,
          day_of_week=day_of_week,
          assists=False,
        )
        logging.error(f"day of week: {assistance.day_of_week}")
        assistance_inserted_id = Repository.add_assistance(assistance)
        logging.error(f"created assistance: {assistance_inserted_id}")
    logging.error(f"REGISTERED SUBJECT ID: {form.vars.id}")
