import vk
import config
session = vk.AuthSession(access_token=input())
vk_api = vk.API(session)

count = 0

def prettify(str):
    while "  " in str:
        str.replace("  "," ")
    if(str[0] == " "):
        str = str[1:]
    if(str[-1] == " "):
        str = str[:-1]
    return  str

summary = open("text.txt","w")

while(True):
    try:
        print(count)
        posts = vk_api.wall.get(domain=config.domain, offset = count)
        if(len(posts[1:]) == 0):
            break;
        for post in posts[1:]:
            text = post['text']
            f = open(config.path+str(count), 'w')
            f.write(text)
            summary.write(text +"\n")
            count+=1
    except:
        continue