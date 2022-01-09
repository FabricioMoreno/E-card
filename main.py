from requests.models import Response
from config import *
import pprint
import sys
import json
from PIL import Image,ImageDraw,ImageFont
import qrcode
#Importando mis módulos
from src.computerVisionApi import *
from src.connectionApi import *
from src.faceApi import *
from src.getInfoDatabase import *
from src.infoCardStundent import *
from src.createQrCode import *
from src.createQrCode import *

#Comenzando al ejecución del programa
url_image_user = input("Ingrese la url de la imagen de la celebridad: ")

#Creando la peteción completa a la COMPUTER VISION API
requests_computer_vision_api = requestsComputerVisionApi(COMPUTER_VISION_API_KEY,url_image_user)
headers_computer_vision_api = requests_computer_vision_api["headers"]
params_computer_vision_api = requests_computer_vision_api["params"]
data_computer_vision_api = requests_computer_vision_api["data"]

#Creando la peteción completa a la FACE API
requests_face_api = requestsFaceApi(FACE_API_KEY,url_image_user)
headers_face_api = requests_face_api["headers"]
params_face_api = requests_face_api["params"] 
data_face_api = requests_face_api["data"]

#Estableciendo conexión con las APIS
computer_vision_api_connection = connectionApi(COMPUTER_VISION_API_URL,headers_computer_vision_api,params_computer_vision_api,data_computer_vision_api)
face_api_connection = connectionApi(FACE_API_URL,headers_face_api,params_face_api,data_face_api)

#Verificando si la conexión a las APIS se completó con éxito
if(computer_vision_api_connection["is_valid"] and face_api_connection["is_valid"]):

  #Obteniedo las respuestas de las APIS
  response_computer_vision = computer_vision_api_connection["response"]
  response_face = face_api_connection["response"]

  invalid_image_messages = []

  #Verficando que la imágen sea válida para la creación del carnet
  if isPerson(response_face):
    if isCelebrity(response_computer_vision):  
      if isCelebrity(response_computer_vision):

        if not isJustFace(response_computer_vision):
          invalid_image_messages.append('No se muestra solo la cara')

        if isWearingGlasses(response_face):
          invalid_image_messages.append("Lleva gafas")

        if isSmiling(response_face):
          invalid_image_messages.append("Está sonriendo")

        if isWearingHatOrCap(response_computer_vision):
          invalid_image_messages.append("LLeva un sombrero")

        if isSillyFace(response_face):
          invalid_image_messages.append("Está haciendo una mueca")


        #Verificando que la imágen haya cumplido con todos los requisitos para ser válida
        if len(invalid_image_messages) == 0:
          name_celebrity = getNameCelebrity(response_computer_vision)
          info_celebrity = getInfoDatabase("./database/celebridades.csv",name_celebrity)

          #Creando el código qr
          location_qr_code = "./qrCode" 
          name_qr_code_file = createQrCode(info_celebrity,location_qr_code)
          info_celebrity["qr_code"] = name_qr_code_file

          #Creando el carnet digital
          info_celebrity["url_img"] = url_image_user
          info_celebrity["gender"] = getGender(response_face)
          print(info_card_student(info_celebrity))
          #createStundetCard(info_card_student(info_celebrity))

        else:
          print("Imagen inválida, razones: ",*invalid_image_messages,sep="\n")  

    else:
      print('La imagen no ha podido ser reconocida')

  else:
    print('La imagen no corresponde a una persona')

elif not computer_vision_api_connection["is_valid"]:
  print(computer_vision_api_connection["response"])

elif not face_api_connection["is_valid"]:
  print(face_api_connection["response"])