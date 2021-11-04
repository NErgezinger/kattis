def score(a, b, c): return(a**2 + b**2 + c**2 + 7 * min(a,b,c))

def highscore2(a, b, c, d):
    nums = sorted([a, b, c])

    if d == 0:
        return score(a, b, c)    

    else:
        lonums = nums[:]
        hinums = nums[:]
        
        lonums[0] += 1
        hinums[2] += 1                  

        if score(*hinums) >= score(*lonums):
            nums[2] += d
            print(nums)
            return(score(*nums))

        hi = highscore2(*hinums, d-1)
        lo = highscore2(*lonums, d-1)
        
        return(max(hi,lo))

n = int(input())
for i in range(n):
    a,b,c,d = list(map(int, input().split()))

    nums = sorted([a, b, c])
    if a == b == c and d == 3:
        print(score(a+1, b+1, c+1))
    elif nums[0] == nums[1] == nums[2]-1 and d == 2:
        print(score(nums[0]+1, nums[1]+1, nums[2]))
    else:
        print(highscore2(a, b, c, d))