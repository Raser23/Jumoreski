from config import GROUPID, OWNERID
from VK import GetGroupUserIds
from Things.DBClient import getClient
import time


def current_users():
    ids = GetGroupUserIds(GROUPID)
    return ids


def add_report():
    current_collection = "Stats"
    db = getClient()
    users = current_users()
    report = {
        "time": time.time(),
        "usersCount": len(users),
        "users": users
    }
    db[current_collection].insert_one(report)
    db.logout()


def get_last_report():
    return get_report(0)


def get_report(num):
    current_collection = "Stats"
    db = getClient()
    # report_count = db[current_collection].count()
    obj = db[current_collection].find().sort('time', -1)[num]

    db.logout()
    return obj


def compare_reports(reportA, reportB):
    AwB = list(set(reportA["users"]) - set(reportB["users"]))
    BwA = list(set(reportB["users"]) - set(reportA["users"]))
    print(AwB)
    print(BwA)
    result = {
        "AwB": AwB,
        "BwA": BwA,
    }
    return result
