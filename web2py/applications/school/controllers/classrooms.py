def index():
  grid = SQLFORM.grid(
    db.classrooms,
    deletable=True,
    editable=True,
    create=False,
    paginate=10,
  )
  return dict(grid=grid)
