total = int(input())
ea = int(input())

sum = 0

for i in range(ea):
    a, b = map(int, input().split())
    sum += a * b
    
if total == sum:
    print("Yes")
else:
    print("No")