from factory.Factory import Factory
from repository.Repository import Repository


class StudentServices:
  @staticmethod
  def register_student(name, grade, age):
    # Create student object using factory
    student = Factory.create_student(name, grade, age)
    # Save student to database using repository
    Repository.add_student(student)
