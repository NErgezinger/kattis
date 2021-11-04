import sys
import math

def prime_factorize_factorial(n):
    prime_divs = set()
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            # print(i, j)
            if (i/j) % 1 == 0: 
                is_prime = False
                break
        if is_prime: prime_divs.add(i)
    
    prime_div_multipl = dict()

    for prime in prime_divs:
        multipl = 0
        for i in range(1, n):
            mult = math.floor(n / (prime ** i))
            if mult == 0: break
            multipl += mult
        
        prime_div_multipl[prime] = multipl
    
    return prime_div_multipl

def prime_factorize(n):
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if (i/j) % 1 == 0: 
                is_prime = False
                break
        if is_prime: primes.append(i)
    
    for p in primes:
        while True:
            if (n/p) % 1 == 0:
                n /= p
            else:
                break
        

for line in sys.stdin:
    n, m = list(map(int, line.split()))

    if m < n:
        div = True
    else:
        prime_fac_n = prime_factorize_factorial(n)
        prime_fac_m = prime_factorize(m)

        div = False
        for p, mul in prime_fac_m.items():
            if p in prime_fac_n and mul < prime_fac_n[p]:
                div = True
                break
            
    

    if div: print(str(m) + " divides " + str(n) + "!")
    else: print(str(m) + " does not divide " + str(n) + "!")