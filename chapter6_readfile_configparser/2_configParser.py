import configparser
config = configparser.RawConfigParser()

config.read_file(open(r'APG1.config'))

# print (config.get('DB Info','DB_USERNAME'))

apgURL = config.get('Rest Info', 'URL')
apgUserName = config.get('Rest Info', 'userName')
apgUserPassword = config.get('Rest Info', 'password')
rpdpodId=config.get('Rest Info', 'podId')

print("URL :", apgURL)
print("User Name : ", apgUserName)

