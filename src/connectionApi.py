import requests

def connectionApi(api_url,http_headers,http_params,data):
  try:
    response = requests.post(api_url,headers=http_headers,params=http_params,json=data,timeout=5)
    response.raise_for_status()

    return {
      "is_valid": True,
      'response': response.json()
    }

  except requests.exceptions.HTTPError:
    return {
      "is_valid": False,
      'response': "Error en la petición del cliente"
    }

  except requests.exceptions.ConnectionError:
    return {
      "is_valid": False,
      'response': "No es posible conectarse al servidor"
    }

  except requests.exceptions.Timeout:
    return {
      "is_valid": False,
      'response': "La solicitud tomó mucho tiempo en completarse"
    }
