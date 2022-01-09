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
  cond_1 = ""
  cond_2 = ""
  PORTRAIT_MAX = 0.6

  for tag_info in response["tags"]:
    if tag_info["name"] == "portrait":
      cond_1 = tag_info["confidence"] >= PORTRAIT_MAX

  for categorieInfo in response["categories"]:
    if categorieInfo["name"] == "people_portrait":
      cond_2 = categorieInfo["score"] >= PORTRAIT_MAX 
        
  return cond_1 or cond_2

def isWearingHatOrCap(response):
  for tag_info in response["tags"]:
    if tag_info["name"] == "cap" or tag_info["name"] == "hat":
      return True
  
  return False
