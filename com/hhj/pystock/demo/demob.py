import requests
url = 'https://gupiao.baidu.com/stock/sz000002.html';
payload = {'key1' : '111'}

headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
requests.get()
print(r.request.headers)