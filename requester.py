import urllib3
http = urllib3.PoolManager()

s = "https://oauth.vk.com/access_token?client_id=6347655&client_secret=jaQfozRp10513b7RaIlL&redirect_uri=https://oauth.vk.com/authorize&code=e1f02ade07c4010c79"

r = http.request('GET', s)
print(r.data)