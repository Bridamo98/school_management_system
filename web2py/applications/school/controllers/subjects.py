def index():
  grid = SQLFORM.grid(
    db.subjects,
    deletable=True,
    editable=True,
    create=False,
    paginate=10,
  )
  return dict(grid=grid)
