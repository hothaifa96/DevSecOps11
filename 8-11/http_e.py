import requests

# res = requests.get('https://www.nike.com',timeout=5)
# print(res.status_code)
# print(res.text)
# print(res.headers)
#
#
#2
payload = {'name':'Donald','last_name':'Trump'}
res2= requests.get('https://httpbin.org/get',params=payload)
print(res2.json())
print(res2.url)

#3
print('*'*140)
payload2={'dream_car':'cupra'}
res3 = requests.post('https://httpbin.org/post',params=payload2)
print(res3.json())