import datetime
import json
import requests
import yagmail

SENDING_EMAIL = "frenchtoastreport@gmail.com"

def adduser(email, name):
    USERS[email] = name
    updateusers()

def updateusers():
    with open("users.json", 'w') as f:
        json.dump(USERS, f)
        f.close()

def getusers():
    global USERS
    with open("users.json", 'r') as f:
        USERS = json.load(f)
        f.close()
    return USERS

def toasttoday():
    menuID = 16
    mealID = 1
    serveDate = str(datetime.date.today())
    url = "https://menuapi.dartmouth.edu:8314/api/HospitalitySuite/publishingGroups/GuestMenuData?menuId="+str(menuID)+"&mealId="+str(mealID)+"&serveDate="+serveDate
    headers = { 'Accept': 'application/json', 'FacilityId':'53 Commons' }
    params = { 'menuId': menuID, 'mealId': mealID, 'serveDate': serveDate}
    response = requests.get(url, headers=headers, params=params)
    json_response = response.json()[0]

    for item in json_response["menuItems"]:
        #print(item['recipe']["description"])
        if item['recipe']["description"].__contains__("French Toast Sticks"):
            return True



if __name__ == '__main__':
    if toasttoday():
        yag = yagmail.SMTP(SENDING_EMAIL)
        for addr, name in getusers().items():
            message = "Good morning {name}! \n\n French Toast Sticks will be served in foco today."
            print("sending mail to:", addr)
            yag.send(addr, "French Toast Stick Report - {date}".format(date=datetime.date.today()), message.format(name=name))
        yag.close()
    else:
        print("No toast today. :( ")
