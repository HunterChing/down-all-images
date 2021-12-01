from urllib.request import urlretrieve

img_url = "https://pbs.twimg.com/media/FFIQlBHWQAsGel0?format=jpg&name=large"
file_name = "./urlretrieve.jpg"

urlretrieve(img_url, file_name)
