from services.business_logic.BusinessLogic import BusinessLogic

def index():
  grid = SQLFORM.grid(
    db.schedules,
    deletable=True,
    editable=True,
    create=True,
    paginate=10,
    user_signature=False,
    oncreate=BusinessLogic.synchronize_assistances_from_schedules
  )
  return dict(grid=grid)