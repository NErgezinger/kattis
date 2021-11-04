setnum = 1
while True:
    
    n = int(input())
    if n == 0:
        break

    print("SET", setnum)
    stack = []
    for i in range(n):
        
        if i%2==0:
            print(input())
        else:
            stack.append(input())

    for i in range(len(stack)):
        print(stack.pop())

    setnum += 1
