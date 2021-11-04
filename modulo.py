nums = set()
for i in range(10):
    n = int(input())
    n = n%42
    nums.add(n)
print(len(nums))
