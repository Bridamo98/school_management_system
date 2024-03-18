from gluon.tools import SQLFORM

from services.api_services.StudentServices import StudentServices


def register_student():
  name = request.vars.name
  grade = request.vars.grade
  age = request.vars.age
  StudentServices.register_student(name, grade, age)
  return response.json({"ok": "Registered student"})
