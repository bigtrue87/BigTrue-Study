t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
 
    # effective cost
    costList = {}
    for i, cost in enumerate(a):
        firUser = cost
        secUser = m - cost 
        if secUser in costList.keys():
            print(costList[secUser]+1,i+1)
        else:
            costList[cost] = i