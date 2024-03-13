from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade = Column(String)
    age = Column(Integer)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class StudentxSubject(Base):
    __tablename__ = 'students_subjects'
    studentId = Column(Integer, ForeignKey('students.id'), primary_key=True)
    subjectId = Column(Integer, ForeignKey('subjects.id'), primary_key=True)
    student = relationship("Student", backref="subjects")
    subject = relationship("Subject", backref="students")

class Classroom(Base):
    __tablename__ = 'classrooms'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class SubjectXClassroom(Base):
    __tablename__ = 'subjects_classrooms'
    subjectId = Column(Integer, ForeignKey('subjects.id'), primary_key=True)
    classroomId = Column(Integer, ForeignKey('classrooms.id'), primary_key=True)
    start = Column(String)
    end = Column(String)
    day = Column(String)
    subject = relationship("Subject", backref="classrooms")
    classroom = relationship("Classroom", backref="subjects")
    __table_args__ = (
        UniqueConstraint('classroomId', 'start', 'end', 'day'),
    )