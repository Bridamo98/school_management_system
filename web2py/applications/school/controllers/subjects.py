def index():
  grid = SQLFORM.grid(
    db.subjects,
    deletable=True,
    editable=True,
    create=True,
    paginate=10,
    user_signature=False,
  )
  return dict(grid=grid)
