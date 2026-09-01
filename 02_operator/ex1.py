a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # 나머지
print(a // b) # 몫
print(a ** b)

# 10 / 3 = 3
# int / int = int

# 복합 대입 연산자
a += 4; print(a)
a -= 2; print(a)

# a++ 없음 이게말이되냐?????

# 비교 연산자
print(3 == 3.0)
print(3 != 4)
print("apple" < "apble")
print(1 < 2 < 3) # 1 < 2 and  2 < 3
print(1 < 3 < 2) # 1 < 3 and 3 < 2

# 논리 연산자
print(True and False)
print(True or False)
print(not True)

# Short-circuit 테스트
a = 10
b = 0
# print(a / b)

if a > 0 or a / b:
    print("yes")
else:
    print("no")

