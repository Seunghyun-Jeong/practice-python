a = []

for i in range(10):
    b = int(input())
    a.append(b % 42)
    
m = set(a)
print(len(m))