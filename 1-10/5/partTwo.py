f = open("./inputTest.txt", "r")
data = {}
intervalles = []
title = ""
for i in f:
    if i.split(':')[0] == "seeds":
        for j in range(0, len(i.split(':')[1].split(" ")[1:]), 2):
            var = i.split(':')[1].split(" ")[1:]
            intervalles.append([int(var[j]), int(var[j]) + int(var[j + 1]),0])
    elif not i[0].isdigit():
        title = i[0:-2]
        data[title] = []
    elif i[0].isdigit():
        data[title].append(i[0:-1].split(" "))
f.close()
intervalles.sort()
print(intervalles)
print(data)


def getFollowing(next, intervalles):
    # destination source range
    intervallesTemp = []
    # pour chaque prochain intervalles, on adapte les intervalles
    for i in range(len(intervalles)):
        for j in range(len(data[next])):
            data[next].sort()
            debSource = int(data[next][j][1])
            finSource = int(data[next][j][1]) + int(data[next][j][2])
            toAdd = int(data[next][j][0]) - debSource
            # print("-------------------")
            # print(debSource, finSource)
            # print(intervalles[i][0], intervalles[i][1])
            # si le début est inférieur à mon intervalle et la fin dans mon intervalle
            if debSource < intervalles[i][0] < finSource < intervalles[i][1]:
                print("test")
                intervallesTemp.append([intervalles[i][0], finSource, intervalles[i][2] + toAdd])
                continue
            # si le début est inférieur à mon intervalle et la fin supérieur à mon intervalle
            elif debSource < intervalles[i][0] < finSource > intervalles[i][1]:
                print("test1")
                intervallesTemp.append([intervalles[i][0], intervalles[i][1], intervalles[i][2] + toAdd])
                continue
            # si le début est supérieur à mon intervalle et la fin dans mon intervalle
            elif intervalles[i][0] < debSource < finSource < intervalles[i][1]:
                print("test2")
                intervallesTemp.append([debSource, finSource, intervalles[i][2] + toAdd])
                continue
            # si le début est dans mon intervalle et la fin supérieur à mon intervalle
            elif intervalles[i][0] < debSource < intervalles[i][1] < finSource:
                print("test3")
                intervallesTemp.append([debSource, intervalles[i][1], intervalles[i][2] + toAdd])
                continue
            # si le début et la fin son supérieur à mon intervalle
            elif debSource > intervalles[i][0] and finSource > intervalles[i][1]:
                continue
    newIntervalles = []

    if len(intervallesTemp) > 0:
        for j in range(len(intervalles)):
            i = 0
            #tant que les intervalles temp sont inf au début de mon intervalle je ne les calcule pas
            while intervallesTemp[i][0] < intervalles[j][0] and i < len(intervallesTemp)-1:
                i += 1
            if i == len(intervallesTemp)-1:
                newIntervalles.append([intervalles[j][0], intervalles[j][1], intervalles[j][2]])
                continue
            if intervallesTemp[i+1][0] > intervalles[j][0]:
                if intervalles[j][1] < intervallesTemp[i][0]:
                    newIntervalles.append([intervalles[j][0], intervalles[j][1], intervalles[j][2]])
                    continue
                else:
                    newIntervalles.append([intervalles[j][0], intervallesTemp[i][0], intervalles[j][2]])
            while intervallesTemp[i][1] < intervalles[j][1] and i < len(intervallesTemp):
                newIntervalles.append([intervallesTemp[i][0], intervallesTemp[i][1], intervallesTemp[i][2]])
                i += 1
            if intervallesTemp[i][1] == intervalles[j][1]:
                continue
            else:
                newIntervalles.append([intervallesTemp[-1][1], intervalles[j][1], intervalles[j][2]])
    else:
        newIntervalles = intervalles
    print(newIntervalles)
    return newIntervalles


print("generating seeds")
seedInt = getFollowing("seed-to-soil map", intervalles)
print(seedInt)
print("generating fertilizer")
fertiInt = getFollowing("soil-to-fertilizer map", seedInt)
print("generating water")
watInt = getFollowing("fertilizer-to-water map", fertiInt)
print("generating light")
ligthInt = getFollowing("water-to-light map", watInt)
print("generating temperature")
tempInt = getFollowing("light-to-temperature map", ligthInt)
print("generating humidity")
humInt = getFollowing("temperature-to-humidity map", tempInt)
print("generating location")
finale = getFollowing("humidity-to-location map", humInt)
print(finale)
