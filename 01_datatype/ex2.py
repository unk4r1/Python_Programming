a = 10
print(a, type(a))

print(bin(a), oct(a), hex(a));
print(ord("A"), chr(65))

x = 10 ** 100
print(x)

a = 2 ** 31 - 1
print(a)
a = a + 1
print(a)

b = 3.14
print(b, type(b))


import sys
print(sys.float_info.min)
print(sys.float_info.max)

print(-sys.float_info.min)
print(-sys.float_info.max)

a = 1.7e308
b = 1.8e308
print(a, b)

print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
print(f"{0.3:.20f}")

print(float(10))
print(int(3.14))
print(float("3.14"))
print(int("123"))
print(int(float("3.14")))
print(str(10))


