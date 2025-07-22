import requests
# https://httpbin.org/#/Cookies/get_cookies
#https://github.com/Ashishgupta361/Python_Api_Testing
# https://rahulshettyacademy.com/
# visit-month
# if we want to sent cookie then it should be dictionary format
cookie = {'visit-month': 'February'}
response = requests.get('http://rahulshettyacademy.com/', cookies=cookie)
# 301 for redirection
print(response.history)
print(response.status_code)

# Redirection
response = requests.get('http://rahulshettyacademy.com/',allow_redirects=False, cookies=cookie)
# 301 for redirection
# output will be 301 because we have set redirection as false, it will not navigate to next page
print(response.status_code)

# Timeout will wait for given time before response
response = requests.get('http://rahulshettyacademy.com/',allow_redirects=False, cookies=cookie,timeout=1)
# 301 for redirection
# output will be 301 because we have set redirection as false, it will not navigate to next page
print(response.status_code)


res = requests.get('https://httpbin.org/cookies',cookies={'visit-year': '2022'})
print(res.text)
print(res.status_code)

se = requests.session()
se.cookies.update({'visit-month': 'February'})
respon = se.get("https://httpbin.org/cookies",cookies={'visit-year': '2022'})
print(respon.text)
print(respon.status_code)