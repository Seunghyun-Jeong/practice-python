import re
p = re.compile('[a-z]+', re.I)

p.match('python')
p.match('Python')
p.match('PYTHON')