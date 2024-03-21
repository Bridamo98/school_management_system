from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Student(Base):  # ok
  __tablename__ = "students"
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  grade = Column(String, nullable=False)
  age = Column(Integer, nullable=False)
  assistances = relationship("Assistance", cascade="all, delete", passive_deletes=True)

  def __init__(self, name, grade, age):
    self.name = name
    self.grade = grade
    self.age = age


class Subject(Base):  # ok
  __tablename__ = "subjects"
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  grade = Column(String, nullable=False)
  schedules = relationship("Schedule", cascade="all, delete", passive_deletes=True)
  assistances = relationship("Assistance", cascade="all, delete", passive_deletes=True)

  def __init__(self, name, grade):
    self.name = name
    self.grade = grade


class Assistance(Base):  # ok
  __tablename__ = "assistances"
  id = Column(Integer, primary_key=True)
  student_id = Column(
    Integer,
    ForeignKey("students.id", ondelete="cascade", onupdate="cascade"),
  )
  subject_id = Column(
    Integer,
    ForeignKey("subjects.id", ondelete="cascade", onupdate="cascade"),
  )
  classroom_id = Column(
    Integer,
    ForeignKey("classrooms.id", ondelete="cascade", onupdate="cascade"),
  )
  week_number = Column(Integer, nullable=False)
  day_of_week = Column(String, nullable=False)
  assists = Column(Boolean, nullable=False)
  __table_args__ = (
    UniqueConstraint(
      "student_id", "subject_id", "classroom_id", "week_number", "day_of_week"
    ),
  )

  def __init__(
    self, student_id, subject_id, classroom_id, week_number, day_of_week, assists
  ):
    self.student_id = student_id
    self.subject_id = subject_id
    self.classroom_id = classroom_id
    self.week_number = week_number
    self.day_of_week = day_of_week
    self.assists = assists


class Classroom(Base):  # ok
  __tablename__ = "classrooms"
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  subjects = relationship("Schedule", cascade="all, delete", passive_deletes=True)
  assistances = relationship("Assistance", cascade="all, delete", passive_deletes=True)

  def __init__(self, name):
    self.name = name


class Schedule(Base):
  __tablename__ = "schedules"
  id = Column(Integer, primary_key=True)
  subject_id = Column(
    Integer,
    ForeignKey("subjects.id", ondelete="cascade", onupdate="cascade"),
  )
  classroom_id = Column(
    Integer,
    ForeignKey("classrooms.id", ondelete="cascade", onupdate="cascade"),
  )
  start_h = Column(String)
  end_h = Column(String)
  day_of_week = Column(String)
  __table_args__ = (
    UniqueConstraint("classroom_id", "start_h", "end_h", "day_of_week"),
  )

  def __init__(self, subject_id, classroom_id, start_h, end_h, day_of_week):
    self.subject_id = subject_id
    self.classroom_id = classroom_id
    self.start_h = start_h
    self.end_h = end_h
    self.day_of_week = day_of_week
