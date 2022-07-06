nums = list(map(int,input().split()))
a = list()
b = list()
for i in nums:
    if i%2 == 0:
        a.append(i)
    else:
        b.append(i)
nums = a+b
print(nums)