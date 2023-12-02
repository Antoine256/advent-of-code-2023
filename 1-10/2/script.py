#1454
#369
f = open("./input.txt", "r")
sum = 0
sum2 = 0
for i in f:
    maxColor = [[0, "red"],[0, "green"],[0, "blue"]]
    splitA = i.split(":")
    split = splitA[1].split(";")
    good = True
    for j in split:
        nbColorTemp = [[0, "red", 12],[0, "green", 13],[0, "blue", 14]]
        for k in j.split(","):
            oneColor = k.split(" ")
            for l in range(0,len(nbColorTemp)):
                if nbColorTemp[l][1] in oneColor[2]:
                    nbColorTemp[l][0] = nbColorTemp[l][0] + int(oneColor[1])
                if maxColor[l][1] in oneColor[2]:
                    if maxColor[l][0] < int(oneColor[1]):
                        maxColor[l][0] = int(oneColor[1])
        for l in range(0,len(nbColorTemp)):
            if nbColorTemp[l][0] > nbColorTemp[l][2]:
                good = False
    mult = 1
    for l in maxColor:
        mult = mult * l[0]
    sum2 = sum2 + mult
    if good:
        sum = sum + int(splitA[0].split(" ")[1])
print(sum)
print(sum2)



