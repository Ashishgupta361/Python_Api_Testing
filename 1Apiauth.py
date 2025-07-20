import requests
from requests.auth import HTTPBasicAuth
from utilities.configurations import *
url = "https://api.github.com/user"
#github_response = requests.get(url, auth=('ashishjhi361@gmail.com',getpwd()))
github_response = requests.get(url, auth=HTTPBasicAuth('ashishjhi361@gmail.com',get_github_token()))
print(github_response)
print(github_response.status_code)
#https://drive.google.com/file/d/18FC3jDnsOol9zn3_KGSrjg35a4unpiSG/view

# if there are SSL error in website then pass parameter verify= false
#github_response = requests.get(url, verify=False, auth=('ashishjhi361@gmail.com',getpwd()))
