import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://www.pinkumall.com/get', params=payload)
# url = www.pinkumall.com
print(type(r))
print(r.status_code)
print(r.encoding)
#print r.text
print(r.cookies)
print(r.url)

