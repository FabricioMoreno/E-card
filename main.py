from requests.models import Response
from config import *
import pprint
import sys

from src.computerVisionApi import *
from src.connectionApi import *
from src.faceApi import *

""" #Importar mis modulos
sys.path.append(f"{ROOT_DIR}/src")
from connectionApi import *
from computerVisionApi import *
from faceApi import * """

url_good_image = "https://assets.teenvogue.com/photos/5988bb10e04ba21beb2a5164/2:3/w_1123,h_1685,c_limit/tom.jpg"
url_bad_image = "https://cloudfront-us-east-1.images.arcpublishing.com/copesa/FFEN3WRTYRH3TE3CIBEWSZRUKI.jpg"
url_bad_image2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Tom_Holland_by_Gage_Skidmore.jpg/1200px-Tom_Holland_by_Gage_Skidmore.jpg"
place_url = "https://github.com/Sambek99/Pyweekend_Photos/blob/main/Torre%20Eiffel.jpg?raw=true"

f = "https://raw.githubusercontent.com/Sambek99/Pyweekend_Photos/main/Foto%206.jpg"
requests_computer_vision_api = requestsComputerVisionApi(COMPUTER_VISION_API_KEY,f)
headers_computer_vision_api = requests_computer_vision_api["headers"]
params_computer_vision_api = requests_computer_vision_api["params"]
data_computer_vision_api = requests_computer_vision_api["data"]

requests_face_api = requestsFaceApi(FACE_API_KEY,f)
headers_face_api = requests_face_api["headers"]
params_face_api = requests_face_api["params"] 
data_face_api = requests_face_api["data"]

computer_vision_api_connection = connectionApi(COMPUTER_VISION_API_URL,headers_computer_vision_api,params_computer_vision_api,data_computer_vision_api)
face_api_connection = connectionApi(FACE_API_URL,headers_face_api,params_face_api,data_face_api)

if(computer_vision_api_connection["is_valid"] and face_api_connection["is_valid"]):
  response_computer_vision = computer_vision_api_connection["response"]
  response_face = face_api_connection["response"]

  """ pprint.pprint(response_computer_vision)
  print('*'*15)
  pprint.pprint(response_face) """
  invalid_image_messages = []
  if isPerson(response_face):
    if isCelebrity(response_computer_vision):    
      print(isJustFace(response_computer_vision))
      print(isWearingGlasses(response_face))
      print(isSmiling(response_face))
      print(isWearingHatOrCap(response_computer_vision))
      print(isSillyFace(response_face))
      print(getNameCelebrity(response_computer_vision))
      
    else:
      print('La imagen no ha podido ser reconocida')
  else:
    print('La imagen no corresponde a una persona')

elif not computer_vision_api_connection["is_valid"]:
  print(computer_vision_api_connection["response"])

elif not face_api_connection["is_valid"]:
  print(face_api_connection["response"])