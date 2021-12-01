import requests

img_url = "https://pbs.twimg.com/media/FFIQlBHWQAsGel0?format=jpg&name=large"
file_name = "./requests_picture.jpg"

result = requests.get(img_url)
with open(file_name, 'wb') as f:
    f.write(result.content)
