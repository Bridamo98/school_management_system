from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



def create_auth_tables() -> None:
  op.create_table(
    "auth_user",
    sa.Column(
      "id",
      sa.INTEGER(),
      server_default=sa.text("nextval('auth_user_id_seq'::regclass)"),
      autoincrement=True,
      nullable=False,
    ),
    sa.Column("first_name", sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column("last_name", sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column("email", sa.VARCHAR(length=512), autoincrement=False, nullable=True),
    sa.Column("password", sa.VARCHAR(length=512), autoincrement=False, nullable=True),
    sa.Column(
      "registration_key", sa.VARCHAR(length=512), autoincrement=False, nullable=True
    ),
    sa.Column(
      "reset_password_key", sa.VARCHAR(length=512), autoincrement=False, nullable=True
    ),
    sa.Column(
      "registration_id", sa.VARCHAR(length=512), autoincrement=False, nullable=True
    ),
    sa.PrimaryKeyConstraint("id", name="auth_user_pkey"),
    postgresql_ignore_search_path=False,
  )

  op.create_table(
    "auth_event",
    sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column("time_stamp", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column("client_ip", sa.VARCHAR(length=512), autoincrement=False, nullable=True),
    sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column("origin", sa.VARCHAR(length=512), autoincrement=False, nullable=True),
    sa.Column("description", sa.TEXT(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(
      ["user_id"],
      ["auth_user.id"],
      name="auth_event_user_id_fkey",
      onupdate="CASCADE",
      ondelete="CASCADE",
    ),
    sa.PrimaryKeyConstraint("id", name="auth_event_pkey"),
  )

  op.create_table(
    "auth_group",
    sa.Column(
      "id",
      sa.INTEGER(),
      server_default=sa.text("nextval('auth_group_id_seq'::regclass)"),
      autoincrement=True,
      nullable=False,
    ),
    sa.Column("role", sa.VARCHAR(length=512), autoincrement=False, nullable=True),
    sa.Column("description", sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint("id", name="auth_group_pkey"),
    postgresql_ignore_search_path=False,
  )
  op.create_table(
    "auth_permission",
    sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column("group_id", sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column("name", sa.VARCHAR(length=512), autoincrement=False, nullable=True),
    sa.Column("table_name", sa.VARCHAR(length=512), autoincrement=False, nullable=True),
    sa.Column("record_id", sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(
      ["group_id"],
      ["auth_group.id"],
      name="auth_permission_group_id_fkey",
      onupdate="CASCADE",
      ondelete="CASCADE",
    ),
    sa.PrimaryKeyConstraint("id", name="auth_permission_pkey"),
  )
  op.create_table(
    "auth_membership",
    sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column("group_id", sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(
      ["group_id"],
      ["auth_group.id"],
      name="auth_membership_group_id_fkey",
      onupdate="CASCADE",
      ondelete="CASCADE",
    ),
    sa.ForeignKeyConstraint(
      ["user_id"],
      ["auth_user.id"],
      name="auth_membership_user_id_fkey",
      onupdate="CASCADE",
      ondelete="CASCADE",
    ),
    sa.PrimaryKeyConstraint("id", name="auth_membership_pkey"),
  )
  op.create_table(
    "auth_cas",
    sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column("created_on", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column("service", sa.VARCHAR(length=512), autoincrement=False, nullable=True),
    sa.Column("ticket", sa.VARCHAR(length=512), autoincrement=False, nullable=True),
    sa.Column("renew", sa.CHAR(length=1), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(
      ["user_id"],
      ["auth_user.id"],
      name="auth_cas_user_id_fkey",
      onupdate="CASCADE",
      ondelete="CASCADE",
    ),
    sa.PrimaryKeyConstraint("id", name="auth_cas_pkey"),
  )


def insert_mocked_data():
  # Insert mocked students
  op.execute("""
      INSERT INTO students (name, grade, age) VALUES
      ('Alice', 'Grade 10', 16),
      ('Bob', 'Grade 11', 17),
      ('Charlie', 'Grade 10', 15)
    """)

  # Insert mocked subjects
  op.execute("""
      INSERT INTO subjects (name, grade) VALUES
      ('Math', 'Grade 10'),
      ('Physics', 'Grade 11'),
      ('Chemistry', 'Grade 10')
    """)

  # Insert mocked classrooms
  op.execute("""
      INSERT INTO classrooms (name) VALUES
      ('Classroom A'),
      ('Classroom B'),
      ('Classroom C')
    """)

  # Insert mocked schedules
  op.execute("""
      INSERT INTO schedules (subject_id, classroom_id, start_h, end_h, day_of_week) VALUES
      (1, 1, '09:00', '10:00', 'Monday'),
      (2, 2, '10:00', '11:00', 'Tuesday'),
      (3, 3, '11:00', '12:00', 'Wednesday')
    """)

  # Create assistances for each student, subject, and classroom combination
  op.execute("""
      INSERT INTO assistances (student_id, subject_id, classroom_id, week_number, day_of_week, assists)
      SELECT
          s.id AS student_id,
          sub.id AS subject_id,
          sch.classroom_id,
          generate_series(1, 52) AS week_number,
          sch.day_of_week AS day_of_week,
          true AS assists
      FROM
          students s
      CROSS JOIN
          subjects sub
      JOIN
          schedules sch ON sub.id = sch.subject_id
      WHERE
          s.grade = sub.grade
    """)
