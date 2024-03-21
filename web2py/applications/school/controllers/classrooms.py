def index():
  grid = SQLFORM.grid(
    db.classrooms,
    deletable=True,
    editable=True,
    create=True,
    paginate=10,
    user_signature=False
  )
  return dict(grid=grid)
