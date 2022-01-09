from os import truncate
from typing import Tuple

from requests.models import Response


def requestsFaceApi(api_key,img_url):
  return{
    "params": {
      "returnFaceId": "false",
      "returnFaceLandmarks": "false",
      "returnFaceAttributes": "headPose, smile, facialHair, glasses, emotion, makeup, occlusion, accessories",
      "recognitionModel": "recognition_01",
      "returnRecognitionModel": "false",
      "detectionModel": "detection_01",
      "faceIdTimeToLive": "86400"
    },
    "headers": {
      "Content-Type": "application/json",
      "Ocp-Apim-Subscription-Key" : api_key
    },
    "data": {
      "url": img_url
    }
  }

def isPerson(response):
  if len(response) == 0:
    return False

  return True

def isWearingGlasses(response):
  glasses_value = response[0]["faceAttributes"]["glasses"]
  if glasses_value == "NoGlasses":
    return False

  return True

def isSmiling(response):
  smile_value = response[0]["faceAttributes"]["smile"]
  SMILE_MAX = 0.5
  if smile_value > SMILE_MAX:
    return True
  
  return False

def isSillyFace(response):
  neutral_face_value = response[0]["faceAttributes"]["emotion"]["neutral"]
  NEUTRAL_FACE_MAX_VALUE = 0.7
  if neutral_face_value >= NEUTRAL_FACE_MAX_VALUE:
    return True
  
  return False