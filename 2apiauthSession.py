import requests
from utilities.configurations import *
url = "https://api.github.com/user"

# session manager
se = requests.session()
se.auth = auth=('ashishjhi361@gmail.com',get_github_token())
#github_response = requests.get(url, auth=('ashishjhi361@gmail.com',getpwd()))
# when we use session object we can replace it with requests and auth is also not required as it already contain auth information.
github_response = se.get(url,)
print(github_response.status_code)
