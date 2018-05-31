# import requests
# from urllib.error import HTTPError, URLError

# def exists(path):
#     r = requests.head(path)
#     return r.status_code == requests.codes == 200

# try:
#     result = exists('https://brainxtech.com/home-icon/Brainx-logo.svg')
# except HTTPError as e:
#     print(e)
# except URLError:
#     print("Server down or incorrect domanin")
# else:
#     print (result)


import httplib2
h = httplib2.Http('.cache')
response, content = h.request('https://brainxtech.com/home-icon/Brainx-logo.svg')
print(response.status)
with open('cow.jpg', 'wb') as f:
    f.write(content)
