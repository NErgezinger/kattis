name = input()
i = 0
while i < len(name)-1:
    if name[i] == name[i+1]: name = name[:i] + name[i+1:] 
    else: i += 1
print(name)