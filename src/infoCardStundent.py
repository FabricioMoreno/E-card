def info_card_student(info):
  return {
  "name": info["nombre"],
  "gender": info["gender"],
  "birthday": info["fecha_nacimiento"],
  "faculty": info["facultad"],
  "degree": info["carrera"],
  "registration": info["matricula"],
  "signature": info["firma"],
  "img": info["url_img"],
  "qr_code": info["qr_code"]
  }