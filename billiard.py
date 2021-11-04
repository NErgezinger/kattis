import math

while(True):
    a, b, s, m, n = map(int, input().split())

    if a + b + s + m + n == 0:
        break
    
    toth = a * m
    totv = b * n

    totdist = math.sqrt((toth**2) + (totv**2))

    ang = math.atan2(totv, toth)
    ang = ang / math.pi * 180

    speed = totdist / s

    print(f"{ang:.2f} {speed:.2f}")
