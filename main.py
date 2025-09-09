import hashlib
s='devnano'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
