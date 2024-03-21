from models.Models import Assistance, Student


class Factory:
  @staticmethod
  def create_student(name, grade, age):
    return Student(name=name, grade=grade, age=age)

  @staticmethod
  def create_assistance(student_id, subject_id, classroom_id, week_number, day_of_week, assists):
    return Assistance(
      student_id=student_id,
      subject_id=subject_id,
      classroom_id=classroom_id,
      week_number=week_number,
      day_of_week=day_of_week,
      assists=assists,
    )
