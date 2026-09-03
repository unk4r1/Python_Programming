i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("End")
    
nums = [1, 3, 5, 7, 9]
target = 2

is_found = 0

while i in nums:
    if i == target:
        found = 1; break
print("found" if is_found else "not found")

i = 1
tot = 0

while i <= 10:
    i += 1
    if i % 2 == 1: continue
    tot += i
else:
    print(f"합: {tot}")
