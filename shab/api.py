import requests
import json


BASE_URL = "http://127.0.0.1:8000/api/v1"


def create_user(username, name, user_id):
    url = f"{BASE_URL}/bot-users"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i["user_id"]== str(user_id):
            user_exist = True
            break
    if user_exist == False:
        data = {
            "username":username,
            "name":name,
            "user_id":user_id
        }
        requests.post(url=url,data=data)
        return "Foydalanuvchi yaratildi"
    else:
        return "Foydalanuvchi mavjud"

# print(create_user("Ali","ishchi","5489544544"))





def Create_profil(user_id,fullname, lavozim, tel, shahar):
    url = f"http://127.0.0.1:8000/api/v1/profillar"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i["user_id"] == user_id:
            user_exist = True
            break
    if user_exist==False and user_id and fullname and lavozim and tel and shahar:
        post = requests.post(url=url, data = {
                "user_id": user_id,
                "fulname": fullname,
                "lavozim": lavozim,
                "tel": tel,
                'shahar':shahar

            })
        return "Profil yaratildi."
    else:
        return 'Profil mavjud.'

def get_profil(user_id):
    url = f"{BASE_URL}/profillar"
    response = requests.get(url=url).text
    data = json.loads(response)
    for i in data:
        if i["user_id"] == str(user_id):
            return i['fulname']

def get_hudud():
    url = f"{BASE_URL}/hududlar"
    response = requests.get(url=url).text
    data = json.loads(response)
    return data

def get_shahar(id):
    tuman = []
    url = f"{BASE_URL}/shaharlar"
    response = requests.get(url=url).text
    data = json.loads(response)
    for i in data:
        if i['hudud']==id:
            tuman.append(i)

    return tuman


def all_profil(shahar):
    all = []
    url = f"{BASE_URL}/profillar"
    response = requests.get(url=url).text
    data = json.loads(response)
    for i in data:
        if i['shahar']==int(shahar):
            all.append(i)
    return all

