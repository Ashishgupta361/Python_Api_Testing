import requests

# https://rahulshettyacademy.com/
# visit-month
# if wee want to sent cookie then it should be dictionary format
cookie = {'visit-month': 'February'}
response = requests.get('https://rahulshettyacademy.com/', cookies=cookie)
print(response.status_code)

res = requests.get('https://httpbin.org/cookies',cookies={'visit-year': '2022'})
print(res.text)
print(res.status_code)

se = requests.session()
se.cookies.update({'visit-month': 'February'})
respon = se.get("https://httpbin.org/cookies",cookies={'visit-year': '2022'})
print(respon.text)
print(respon.status_code)