def findmin(v):
    denominations = [1,2,5,10,20,50,100,500,1000]
    n = len(denominations)
    ans = []
    i = n - 1
    while(i >= 0):
        while(v >= denominations[i]):
            v -= denominations[i]
            ans.append(denominations[i])
        i -= 1

    for i in range(len(ans)):
        print(ans[i], end=" ")

if __name__ == '__main__':
    n = 93
    findmin(n)
