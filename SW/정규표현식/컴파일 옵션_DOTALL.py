# DOTALL, S
# DOT(.) 문자가 줄바꿈 문자도 포함하도록 만드는 옵션

import re
p=re.compile('a.b', re.DOTALL)
m=p.match('a\nb')
print(m)