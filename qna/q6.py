a = input('숫자를 입력하세요 : ')
num = a.split(',')
result = 0
for n in num:
    result += int(n)

print(result)
