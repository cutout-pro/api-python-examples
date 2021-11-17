import requests
import base64, json
import config
import time
import utils
print(config.API_BASE_URL)

url = config.API_BASE_URL + '/api/v1/idphoto/printLayout'
apikey = config.API_KEY
headers={'APIKEY': apikey, "Content-type": "application/json"}
file = "input/idphoto.jpg"
with open(file, mode='rb') as f:
  #base64 binary
  base64_binary = base64.b64encode(f.read())
  #Use utf-8 encoding to convert binary to string
  base64_str = base64_binary.decode(encoding = "utf-8")
  # print(base64Str)
  data = {
    "base64": base64_str, #Base64 of portrait image file
    "bgColor": "438EDB",#The background color of the ID photo, the format is hexadecimal RGB, such as: 3557FF
    "dpi": 300, #ID photo printing dpi, generally 300
    "mmHeight": 35, #The physical height of the ID photo, in millimeters
    "mmWidth": 25, #The physical width of the ID photo, in millimeters
    "printBgColor": "FFFFFF", #Typesetting background color, the format is hexadecimal RGB, such as: FFFCF9
    "printMmHeight": 152, #The size of the printed layout, in millimeters, if it is 0 or smaller than the size of the ID photo, the layout will not be performed, and a single ID photo will be output.
    "printMmWidth": 102, #The size of the printed layout, in millimeters, if it is 0 or smaller than the size of the ID photo, the layout will not be performed, and a single ID photo will be output.
    "dress": "man8", #The dressing parameter is not required. If there is no parameter, the dressing is not changed. It is in the format of type + dressing number. For example, man1 is the first dressup picture for men, woman3 is the third dressup for women, and child5 is the fifth dressup for children. An extra point will be deducted for the change
    "printMarginMm":5 #The size of the external reserved space of the printed typesetting, not required
  }
  response = requests.post(url=url, headers=headers, json=data)
  content = response.content.decode(encoding = "utf-8")
  print(content)
  json_result = json.loads(content)
  if json_result["code"] == 0:
    image_url = json_result["data"]["idPhotoImage"]
    file_name = './output/idphoto'+time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())+".jpg"
    utils.download_img(image_url,file_name)
