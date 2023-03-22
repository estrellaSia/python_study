import re
p=re.compile('[a-z]+')
m=p.finditer('life is too short')
for r in m:
    print(r)