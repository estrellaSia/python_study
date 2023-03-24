# 전방탐색: 긍정형 (?=)
# http: -> http
import re
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

# 전방탐색: 부정형 (?!)
import re
p = re.compile(".*[.](?!bat$|exe$).*$", re.M)
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)