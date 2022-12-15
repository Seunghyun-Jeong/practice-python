f = open('sample.txt', 'w')
f.write('''
70
60
55
75
95
90
80
80
85
100
''')
f.close()

f = open('sample.txt', 'r')
lines = f.readlines()
f.close()

add = 0
average = 0
for line in lines:
    score = float(line)
    add += score
average = add / len(lines)

f = open('result.txt', 'w')
f.write(str(average))
f.close()