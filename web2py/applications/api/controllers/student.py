def obtener_datos():
  datos = {"mensaje": "Estos son algunos datos de ejemplo"}
  return response.json(datos)


def enviar_datos():
  datos_recibidos = request.vars.get("datos")
  return response.json({"mensaje": f"Datos recibidos: {datos_recibidos}"})
