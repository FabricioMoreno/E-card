from config import *
import sys
#Importar mis modulos
sys.path.append(f"{ROOT_DIR}/src")
from connectionApi import *

url_good_image = "https://assets.teenvogue.com/photos/5988bb10e04ba21beb2a5164/2:3/w_1123,h_1685,c_limit/tom.jpg"
url_bad_image = "https://cloudfront-us-east-1.images.arcpublishing.com/copesa/FFEN3WRTYRH3TE3CIBEWSZRUKI.jpg"

params = {
  "visualFeatures": "Categories",
  "details": "Celebrities",
  "language": "en",
  "model-version": "latest"
}

headers = {
  "Content-Type": "application/json",
  "Ocp-Apim-Subscription-Key" : API_KEY
}

data = {
  "url": url_good_image
}


connection = connectionApi(API_URL,headers,params,data)

if(connection['is_valid']):
  print(connection['response'])
else:
  print(connection['response'])