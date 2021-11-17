import requests
import base64, json
import config
import time
import urllib.parse

print(config.API_BASE_URL)


# Mode 1: Return binary image file
def matting(matting_type):
  url_params = {
    "mattingType":matting_type, #Cutout type, 1: Portrait, 2: Object, 3: Portrait, 4: One-click beautification, 6: General cutout, 11: Cartoon.
  }
  query_str = urllib.parse.urlencode(url_params)
  url = config.API_BASE_URL + '/api/v1/matting?'+query_str

  apikey = config.API_KEY
  response = requests.post(
      url,
      files={'file': open('input/idphoto.jpg', 'rb')},
      headers={'APIKEY': apikey},
  )
  file_name = './output/matting1-'+time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())+".jpg"
  with open(file_name, 'wb') as out:
      out.write(response.content)

#Mode 2: Return data in json format, and the picture data is a base64 encoded string
def matting2(matting_type):
  url_params = {
    "mattingType": matting_type,  # Cutout type, 1: Portrait, 2: Object, 3: Portrait, 4: One-click beautification, 6: General cutout, 11: Cartoon.
  }
  query_str = urllib.parse.urlencode(url_params)
  url = config.API_BASE_URL + '/api/v1/matting2?' + query_str
  apikey = config.API_KEY
  response = requests.post(
      url,
      files={'file': open('input/idphoto.jpg', 'rb')},
      headers={'APIKEY': apikey},
  )

  content = response.content.decode(encoding = "utf-8")
  print(content)
  json_result = json.loads(content)
  if json_result["code"] == 0:
    image_base64 = json_result["data"]["imageBase64"]
    base64_binary = base64.b64decode(image_base64)
    file_name = './output/matting2-'+time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())+".png"
    with open(file_name, 'wb') as out:
        out.write(base64_binary)

#Mode 2: Pass the picture url address as a parameter, return json format data, and the picture data is a base64 encoded string
def mattingByUrl(matting_type):
  url = config.API_BASE_URL + '/api/v1/mattingByUrl'
  test_image_url = "http://deeplor.oss-cn-hangzhou.aliyuncs.com/upload/image/20200903/1705c25fa2884cb282ef2be77ec516ef.jpg"
  url_params = {
    "mattingType": matting_type,  # Cutout type, 1: Portrait, 2: Object, 3: Portrait, 4: One-click beautification, 6: General cutout, 11: Cartoon.
    "url": test_image_url #Picture url address
  }
  url = config.API_BASE_URL + '/api/v1/mattingByUrl'
  apikey = config.API_KEY
  response = requests.get(
    url,
    params=url_params,
    headers={'APIKEY': apikey},
  )

  content = response.content.decode(encoding="utf-8")
  print(content)
  json_result = json.loads(content)
  if json_result["code"] == 0:
    image_base64 = json_result["data"]["imageBase64"]
    base64_binary = base64.b64decode(image_base64)
    file_name = './output/mattingByUrl-' + time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime()) + ".png"
    with open(file_name, 'wb') as out:
      out.write(base64_binary)
if __name__ == '__main__':
  matting(matting_type=11)
  matting2(matting_type=11)
  mattingByUrl(matting_type=11)
