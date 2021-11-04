def score(nums):
    a = nums[0]
    b = nums[1]
    c = nums[2]
    return(a**2 + b**2 + c**2 + 7 * min(a,b,c))

n = int(input())

for i in range(n):
    a, b, c, d = list(map(int, input().split()))
    nums = [a,b,c]
    for i in range(d):

        nums = sorted(nums)
        hinums = nums[:]
        lonums = nums[:]

        lonums[0] += 1
        hinums[2] += 1
        
        if score(hinums) - score(nums) > score(lonums) - score(nums):
            nums[2] += d-i
            break
        else:
            nums[0] += 1

    print(score(nums))