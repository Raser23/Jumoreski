import vk
import config
session = vk.AuthSession(access_token=config.AT)
vk_api = vk.API(session)

count = 0
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
            count+=1
    except:
        continue