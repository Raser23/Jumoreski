import hashlib

def hash_string(text):
    return hashlib.md5(str(text).encode('utf-8')).hexdigest()

print(hash_string("1234"))