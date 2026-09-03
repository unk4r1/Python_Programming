# for문

# for (int i = 0; i <= 10; i++)

for i in range(5):
    print(i, end = " ")
print()

a = range(5)
print(a.start, a.stop, a.step)

for i in range(1, 5):
    print(i, end = " ")
print()

# 0 ~ 10까지 숫자 중 짝수
for i in range(0, 11, 2):
    print(i, end = " ")
print()

for i in range(5, 0, -1):
    print(i, end = " ")
print()

tot = 0
for i in range(1, 11):
    tot += i
else: print(tot)

print(sum(range(1, 11)))

s = "hi12!@한글öä😂"

for c in s:
    print(c, end = " ")
    
print(len(s))

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}", end="   ")
    print()
