import os

domain = "jumoreski"
path = "aneks/"
#dvach
TOKEN = os.environ.get('TOKEN')
VKTOKEN = os.environ.get('VKAPI')
DEBUGID = os.environ.get('DEBUGID')
OWNERID = os.environ.get('OWNERID')
WH = os.environ.get('WH')
DBURL = os.environ.get("DBURL")
print(DBURL)
MINLIKES = -1
POSTCD = 60 * 45

UPDATETIME = 60 * 10
HOST = 'https://jumoreski.herokuapp.com'