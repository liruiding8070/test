import requests

url = "http://www.baidu.com"

# resp = requests.get(url)
# resp.encoding = "utf-8"
# print(resp)

# data = {
#     'form': 'zh',
#     'to': 'en',
#     'query': '人生苦短，我用python'
# }
# response = requests.post(url, data=data)
# response.encoding = "utf-8"
# print(response.text)

r = requests.get(url = 'http://itwhy.org')
print(r.status_code)
r=requests.get(url='http://dict.baidu.com/s',params = {'wd':'python'})
print(r.url)
print(r.text)
