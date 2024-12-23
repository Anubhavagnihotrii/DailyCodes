
def frequencyCount(arr):
    countSum=[0] * (len(arr))
    print(countSum)
    for i in arr:
        countSum[i-1]+=1
    return countSum

print(frequencyCount([1,1,1,1]))