shift=1

while shift > 0:
    inp = input().split()   

    shift = int(inp[0])

    if shift == 0:
        break

    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

    rev = inp[1][::-1]
    
    for a in rev:
        ind = alph.find(a)
        print(alph[(ind + shift) % 28], end='')

    print()

    
