import requests, json
import readAPGinfo

url=readAPGinfo.rpgURL
username=readAPGinfo.rpgUserName
password=readAPGinfo.rpgUserPassword

# get APG
def getAction(url):
    response = requests.get(url, auth=requests.auth.HTTPBasicAuth(username, password))
    if response.status_code == 200:
        data = response.json()
    else:
        print("APG Get Failed")
    return data

def dequeItemsInJson(sourcedata):
    newAct = {}
    print("*** List of Accounts to be provisioned ***")
    i=1
    for items in sourcedata:
        print(items["id"])
        print(items["accountName"])
        print(items["action"])
        print(items["status"])
        print("End of item : ",i)
        print("**********")
        i=i+1

def main():
    data = getAction(url)
    #print(data)
    dequeItemsInJson(data)

main()
