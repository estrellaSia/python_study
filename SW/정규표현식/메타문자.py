# 메타문자 |
# or과 동일한 의미
import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

# 메타문자 ^
# 문자열의 맨 처음과 일치함
import re
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))

# 메타문자 $
# 문자열의 끝과 매치(메타문자 ^와 반대)
import re
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))

# 메타문자 b
# 단어 구분자
# 주의) \b는 파인썬 리터럴 규칙에 의하면 백스페이스를 의미하므로 백스페이스가 아닌 단어 구분자임을 알려주기 위해 기호r(Raw string)을 반드시 붙여줘야 함
import re
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))


