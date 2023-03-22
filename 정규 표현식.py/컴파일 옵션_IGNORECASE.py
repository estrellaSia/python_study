# IGNORECASE, I
# 대소문자를 다 무시하고 matching할 수 있도록 해주는 옵션

import re
p = re.compile('[a-z]', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))