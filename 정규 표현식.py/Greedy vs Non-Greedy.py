# Greedy
import re
s = '<html><head><title>Title</title>'
print(re.match('<.*>', s).group())

# Non-Greedy
import re
s = '<html><head><title>Title</title>'
print(re.match('<.*?>', s).group())
