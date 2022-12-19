import re

p = re.compile("[a-z]+")
m = p.search("5 python")
m.start() + m.end()