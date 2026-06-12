def add(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

print(add(10, 20, 30, 40))
print(add(10, 20, 30, 100)) 