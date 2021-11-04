xs, ys, ss, ri, rf = list(map(int, input().split()))
xa, ya, sa = list(map(int, input().split()))

da = ((xs-xa)**2 + (ys-ya)**2)**.5
da = da - rf
ds = ri - rf

ta = da * sa
ts = ds * ss

#print(ta, da)
#print(ts, ds)

if da > ds and sa <= ss:
    #print("ta")
    print("%.6f" % ta)
elif da <= ds and sa >= ss:
    #print(0)
    print("%.6f" % 0)
elif da <= ds and sa <= ss:
    #print("ta-ts")
    print("%.6f" % (ta-ts))
elif da >= ds and sa >= ss:
    #print("ts-ta")
    print("%.6f" % (ts-ta))