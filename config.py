import os

domain = "jumoreski"
path = "aneks/"
TOKEN = os.environ.get('TOKEN')

VKAPIGROUP = os.environ.get('VKAPIGROUP')
VKAPIUSER = os.environ.get('VKAPIUSER')

DEBUGID = os.environ.get('DEBUGID')
OWNERID = os.environ.get('OWNERID')
WH = os.environ.get('WH')
DBURL = os.environ.get("DBURL")
MINLIKES = -1
VKPOSTING = True
POSTCD = 60 * 45
DBCLIENT = os.environ.get('DBCLIENT')
GROUPID = os.environ.get('GROUPID')
VKOWNERID = os.environ.get('VKOWNERID')
VKAPIVERSION = os.environ.get('VKAPIVERSION')

REPORTTIME = 60 * 60 * 12


UPDATETIME = 60 * 10
HOST = 'https://jumoreski.herokuapp.com'

print(VKTOKEN)