import re

p = re.compile('정규표현식')
m = p.match('string goes here')
if m:
    print('Match found: ', m.group())
else:
    print('No match')