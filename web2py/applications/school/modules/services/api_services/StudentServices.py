import logging
from factory.Factory import Factory
from repository.Repository import Repository


class StudentServices:
  @staticmethod
  def register_student(name, grade, age) -> str:
    # Create student object using factory
    student = Factory.create_student(name=name, grade=grade, age=age)
    # Save student to database using repository
    student_inserted_id = Repository.add_student(student)
    logging.error(f"inserted_id: {student_inserted_id}")
    subjects_ids = Repository.get_subject_ids_by_grade(grade)
    logging.error(f"subjects_ids: {subjects_ids}")
    if len(subjects_ids) == 0:
      return "There is no subjects for the specified grade"

    registered_subjects = ""
    for subject_id in subjects_ids:
      registered_subjects += f"{subject_id},"
      classrooms_ids = Repository.get_classroom_ids_and_dow_by_subject_id_on_schedules(
        subject_id
      )
      logging.error(f"classrooms_ids: {classrooms_ids}")
      for (classroom_id, day_of_week) in classrooms_ids:
        for week in range(1, 53):
          assistance = Factory.create_assistance(
            student_id=student_inserted_id,
            subject_id=subject_id,
            classroom_id=classroom_id,
            week_number=week,
            day_of_week=day_of_week,
            assists=False,
          )

          assistance_inserted_id = Repository.add_assistance(assistance)
          logging.error(f"created assistance: {assistance_inserted_id}")


    return f"Registered subjects: {registered_subjects}"
