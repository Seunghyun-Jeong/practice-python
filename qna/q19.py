import re

s = '''
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
'''

p = re.compile(r'(\w+\s+\d+[-]\d+)[-]\d+')
m = p.sub('\g<1>-####', s)
print(m)