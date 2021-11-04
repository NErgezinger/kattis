import sys
import random

#sys.setrecursionlimit(100000)

#n = int(input())

def score(a, b, c):
    if a <= b and a <= c:
        return(a**2 + b**2 + c**2 + 7 * a)
    if b <= c:
        return(a**2 + b**2 + c**2 + 7 * b)
    else:
        return(a**2 + b**2 + c**2 + 7 * c)

memo = {}
def highscore(a, b, c, d):
    abcd = (a,b,c,d)
    if d == 0:
        memo[abcd] = score(a, b, c)
        return score(a, b, c)
    else:
        if abcd in memo:
            return memo[abcd]
        maxa = a
        mina = a
        maxb = b
        minb = b
        maxc = c
        minc = c

        if a >= b and a >= c:
            maxa += 1
        elif b >= c:
            maxb += 1
        else:
            maxc += 1
        
        if a <= b and a <= c:
            mina += 1
        elif b <= c:
            minb += 1
        else:
            minc += 1             

        hi = highscore(maxa, maxb, maxc, d-1)
        lo = highscore(mina, minb, minc, d-1)

        if hi > lo:
            memo[abcd] = hi
            return(hi)
        else:
            memo[abcd] = lo
            return(lo)


def highscore2(a, b, c, d):
    nums = sorted([a, b, c])
    if d == 0:
        return score(a, b, c)
    elif a == b == c and d == 3:
        return(score(a+1, b+1, c+1))
    elif nums[0] == nums[1] and nums[1] == nums[2]-1 and d == 2:
        return(score(nums[0]+1, nums[1]+1, nums[2]))
    else:
        mina = a
        minb = b
        minc = c
        
        if mina < minb and mina < minc:
            mina += 1
        elif minb < minc:
            minb += 1
        else:
            minc += 1 

        if a > b and a > c:
            a += 1
        elif b > c:
            b += 1
        else:
            c += 1                    

        if score(a, b, c) >= score(mina, minb, minc):
            if a > b and a > c:
                a += d-1
            elif b > c:
                b += d-1
            else:
                c += d-1
            return(score(a, b, c))

        hi = highscore2(a, b, c, d-1)
        lo = highscore2(mina, minb, minc, d-1)
        
        if hi > lo:
            return hi
        else:
            return lo

n = int(input())
for i in range(n):
    a,b,c,d = list(map(int, input().split()))

    print()
    print(highscore(a, b, c, d))
    print(highscore2(a, b, c, d))
    #print(memo)

# i = 0
# while True:
#     i += 1
    
#     d = random.randint(0,5)
#     a = random.randint(0,100)
#     b = random.randint(0,100)
#     c = random.randint(0,100)

#     score1 = highscore(a, b, c, d)
#     score2 = highscore2(a, b, c, d)

#     print()
#     print(a, b, c, d)
#     print(score1)
#     print(score2)
#     print("Checked", i)

#     if score1 != score2:
#         break