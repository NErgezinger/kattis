import math
from collections import deque

n, reqPerSecond = list(map(int, input().split()))

requests= []
for i in range(n):
    requests.append(int(input()))

currentRequests = deque()
maxLen = 0

for i, request in enumerate(requests):

    currentRequests.append(request)

    while True:
        if request - 1000 >= currentRequests[0]:
            currentRequests.popleft()
        else:
            break

    #print(currentRequests)

    if len(currentRequests) > maxLen:
        maxLen = len(currentRequests)

print(math.ceil(maxLen/reqPerSecond))