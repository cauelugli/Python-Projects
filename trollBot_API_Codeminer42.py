import requests
from random import randint

randomNames = ["ice_cream_fusion","poop_poop","nuclear_android","allergies_male","elevator_trees","whale_floppy_disk","crab_cone","breakfast_drugs","prints_hnads","comics_bird",
               "nuclear_shower","dislike_youtube","websites_video_games","monster_bird","rollers_rollers","water_mail","towel_boat","system_floppy_disk","ice_cream_cone_allergies","book_clock",
               "bbq_toolbox","puppy_android","dislike_solar","floppy_disk_rollers","male_website","shoes_leash","breakfast_bird","sink_clock","shoe_water","shoes_dislike"]

class Instance:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printfunc(self):
        print("\nID:", self.id,
              "\nName:", self.name)


def postfunc(id, newname):
    person = {
        'name': newname,
        'age': 999,
        'gender': 'M',
        'lonlat': 'POINT (99.9 88.8)'
    }
    requests.patch(f'http://zssn-backend-example.herokuapp.com/api/people/{id}.json', json=person)
    print("\nChanged!")

def gettargetlist():
    urlGet = requests.get('http://zssn-backend-example.herokuapp.com/api/people.json')
    targetList = []
    baseGetUrl = urlGet.json()
    #print("\nAvailable names:\n")
    for h in baseGetUrl:
        name = h["name"]
        #print(name)
        targetList.append(name)
    targetName = targetList[randint(0, 9)]
    for i in baseGetUrl:
        id = i["location"].replace('http://zssn-backend-example.herokuapp.com/api/people/', '')
        name = i["name"]
        targetList.append(i["name"])
        if targetName in name:
            print(f'\nFound {targetName}')
            newname = randomNames[randint(0, 29)]
            postfunc(id, newname)
            break


while True:
    gettargetlist()


