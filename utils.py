import urllib.request

def download_img(img_url, file_name):
    try:
        request = urllib.request.Request(img_url)
        response = urllib.request.urlopen(request)
        if (response.getcode() == 200):
            with open(file_name, "wb") as f:
                f.write(response.read()) # Write content to picture
            return file_name
    except:
        return "failed"