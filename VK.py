import config as CFG
import vk




def GetUserGroups(userId):
    counter = 0
    errorCounter = 0
    while True:
        try:
            if(errorCounter >= 20):
                print("skipped")
                return []

            result = api.users.getSubscriptions(user_id = userId)['groups']['items']
            return result
        except:
            errorCounter +=1
            pass

def GetGroupUserIds(groupId , count = -1):
    loadCount = 100
    first={}
    while True:
        try:
            first = api.groups.getMembers(group_id = groupId,offset = 0, count = loadCount)
            break
        except:
            pass

    userIds = first['users']

    maxCount = first['count']
    if(count >= 0):
        maxCount = min(maxCount, count)

    loadedUsers = 0

    while loadedUsers < maxCount:
        print(str(loadedUsers)+" / "+str(maxCount))
        try:
            loadedUsers = len(userIds)
            userIds = userIds + api.groups.getMembers(group_id = groupId,offset = loadedUsers, count = loadCount)['users']
        except:
            pass

    return userIds

def textUserGroups(groups):
    text =""
    for g in groups:
        text = text + str(g) +" "
    return text

def GetMostPopularGroups(userIds ,isGood, maxCount = 5000):

    groupCount = 0
    groups = {}

    getted = 0
    print((userIds))
    for id in userIds:
        print(id)
        while True:
            try:
                a = GetUserGroups(id)
                print((a))
                for group in a:

                    if group in groups:
                        #print(groups)
                        groups[group] += 1
                    else:
                        if(groupCount < maxCount):
                            groups[group] = 1
                        else:
                            pass
                break
            except:
                pass
        getted +=1

        #print("get: " + str(getted))
    return [a for a in groups]

def SaveUser(isGood, userId ,fileName):
    a=[]
    while True:
        try:
            a = GetUserGroups(userId)
            break
        except:
            pass
    text = textUserGroups(a)

    path = 'Data/'
    if(isGood):
        path = path + 'White/'
    else:
        path = path + 'Black/'
    path = path + fileName +'.txt'
    with open(path, 'w') as f:
        f.write(text)

def SaveUsers(isGood, userIds):
    import time

    startName = time.time()
    counter = 0

    for idn in userIds:
        SaveUser(isGood,idn,str(startName + counter))
        counter +=1

def GetUserById(id):
    errorCount = 0
    while True:
        try:
            if(errorCount > 20):
                return [{'uid': 91304376, 'first_name': 'Алексей', 'last_name': 'Филин'}]
            return (api.users.get(user_ids = id))
        except:
            errorCount+=1

def Start():
    global session
    global api
    session = vk.AuthSession(access_token = CFG.VKTOKEN)
    #print(CFG.VKTOKEN)
    api = vk.API(session)



Start()

#print(GetUserById("alekseifilin"))
#print(GetUserGroups(0))