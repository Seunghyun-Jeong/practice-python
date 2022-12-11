import re

p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes')
p.sub('colour', 'blue socks and red shoes', count = 1)
p.subn('colour', 'blue socks and red shoes')