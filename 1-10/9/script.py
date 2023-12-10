f = open("./input.txt", "r")
sum = 0
def fullZero(data):
    res = True
    for i in data:
        if i != 0:
            res = False
    return res

def getFollowing(data):
    if fullZero(data[1]):
        return int(data[0][-1])
    else:
        return int(data[0][-1]) + getFollowing(data[1:])

def getPrevious(data):
    if fullZero(data[1]):
        return int(data[0][0])
    else:
        return int(data[0][0]) - getPrevious(data[1:])

for i in f:
    print(i)
    data = []
    data.append(i.split())
    while not fullZero(data[-1]):
        newLine = []
        for j in range(0, len(data[-1])-1, 1):
            newLine.append(int(data[-1][j+1]) - int(data[-1][j]))
        data.append(newLine)
    sum += getPrevious(data)
    print(data)
print(sum)
