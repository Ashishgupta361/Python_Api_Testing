import configparser
def getconfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

def get_github_token():
    with open('C:\\Users\\91998\\Documents\\token_github.txt','r') as token:
        t = token.readline()
    return t

