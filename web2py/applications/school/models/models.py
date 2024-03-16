from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade = Column(String)
    age = Column(Integer)
    subjects = relationship("StudentxSubject", cascade="all, delete", passive_deletes=True)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    classrooms = relationship("SubjectXClassroom", cascade="all, delete", passive_deletes=True)
    students = relationship("StudentxSubject", cascade="all, delete", passive_deletes=True)

class StudentxSubject(Base):
    __tablename__ = 'students_subjects'
    student_id = Column(Integer, ForeignKey('students.id', ondelete="cascade", onupdate="cascade"), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete="cascade", onupdate="cascade"), primary_key=True)

class Classroom(Base):
    __tablename__ = 'classrooms'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subjects = relationship("SubjectXClassroom", cascade="all, delete", passive_deletes=True)

class SubjectXClassroom(Base):
    __tablename__ = 'subjects_classrooms'
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete="cascade", onupdate="cascade"), primary_key=True)
    classroom_id = Column(Integer, ForeignKey('classrooms.id', ondelete="cascade", onupdate="cascade"), primary_key=True)
    start_h = Column(String)
    end_h = Column(String)
    day_of_week = Column(String)
    __table_args__ = (
        UniqueConstraint('classroom_id', 'start_h', 'end_h', 'day_of_week'),
    )