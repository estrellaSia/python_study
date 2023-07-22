# MULTILINE, M
# ^를 맨처음만이 아닌 각 라인에 처음으로 인식시키는 옵션


import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))