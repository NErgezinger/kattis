def checkBalance(s):
    W = 0
    B = 0
    for stone in s:
        if stone == 'W':
            W += 1
        else:
            B += 1
    return(W == B)


stones = input()

balanced = False

balanced = checkBalance(stones)

while not balanced:
    
