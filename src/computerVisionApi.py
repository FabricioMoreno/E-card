def requestsComputerVisionApi(api_Key,img_url):
  return{
    "params": {
      "visualFeatures": "Tags",
      "details": "Celebrities",
      "language": "en",
      "model-version": "latest"
   },
    "headers": {
      "Content-Type": "application/json",
      "Ocp-Apim-Subscription-Key" : api_Key
    },
    "data": {
      "url": img_url
    }
  }

def isCelebrity(response):
  for categorieInfo in response["categories"]:
    if "detail" in categorieInfo:
      if "celebrities" in categorieInfo["detail"]:
        if len(categorieInfo["detail"]["celebrities"]) > 0:
          return True

  return False

def getNameCelebrity(response):
  name_celebrity = response["categories"][0]["detail"]["celebrities"][0]["name"]
  
  return name_celebrity

def isJustFace(response):
  for categorieInfo in response["categories"]:
    if categorieInfo["name"] == "people_portrait":
      PORTRAIT_MAX = 0.6
      if categorieInfo["score"] >= PORTRAIT_MAX:
        return True
      else:
        return False

  return False

def isWearingHatOrCap(response):
  for tag_info in response["tags"]:
    if tag_info["name"] == "cap" or tag_info["name"] == "hat":
      return True
  
  return False
