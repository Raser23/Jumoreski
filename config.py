import os

domain = "jumoreski"
path = "aneks/"
TOKEN = os.environ.get('TOKEN')

VKAPIGROUP = os.environ.get('VKAPIGROUP')
VKAPIUSER = os.environ.get('VKAPIUSER')

VKB = os.environ.get('VKB')
VKF = os.environ.get('VKF')

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

REPORTTIME = 60 * 60 * 24


UPDATETIME = 60 * 10
HOST = 'https://jumoreski.herokuapp.com'

#Collection names
collections = {}
collections["hum"] = "anekdotes"
collections["lent"] = "Lentyach"
collections["kal"] = "Kalik"

#Domain names
domains = {}
domains["hum"] = "jumoreski"
domains["lent"] = "lentyay_tv"
domains["kal"] = "kalikfan"

#Model names
models = {}
models["hum"] = "hum_model"
models["lent"] = "lent_model"
models["kal"] = "kal_model"