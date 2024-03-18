from models.Models import Student
from gluon import current


class Repository:
  @staticmethod
  def add_student(student: Student):
    db = current.globalenv["db"]
    db["students"].insert(name=student.name, grade=student.grade, age=student.age)
