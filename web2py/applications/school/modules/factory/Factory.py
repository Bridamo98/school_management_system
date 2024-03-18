from models.Models import Student


class Factory:
  @staticmethod
  def create_student(name, grade, age):
    return Student(name=name, grade=grade, age=age)
