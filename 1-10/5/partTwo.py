f = open("./inputTest.txt", "r")
data = {}
intervalles = []
title = ""
for i in f:
    if i.split(':')[0] == "seeds":
        for j in range(0, len(i.split(':')[1].split(" ")[1:]), 2):
            var = i.split(':')[1].split(" ")[1:]
            intervalles.append([int(var[j]), int(var[j]) + int(var[j + 1])])
    elif not i[0].isdigit():
        title = i[0:-2]
        data[title] = []
    elif i[0].isdigit():
        data[title].append(i[0:-1].split(" "))
f.close()
intervalles.sort()
print(intervalles)
print(data)
tab = {}
for i in data["seeds"]:
    tab[i] = [i]


def getFollowing(next):
    # destination source range
    data[next].sort()
    intervallesTemp = []
    #pour chaque prochain intervalles on adapte les intervalles
    for i in range(len(data[next])):
        debSource = int(data[next][i][1])
        finSource = int(data[next][i][1]) + int(data[next][i][2])
        for j in range(len(intervalles)):
            if :
                add = int(data[next][j][0]) - int(data[next][j][1])
                intervallesTemp.append([intervalles[i][0] + add , intervalles[i][1] + add])
                break





print("generating seeds")
getFollowing("seed-to-soil map"),
print("generating fertilizer")
getFollowing("soil-to-fertilizer map"),
print("generating water")
getFollowing("fertilizer-to-water map"),
print("generating light")
getFollowing("water-to-light map"),
print("generating temperature")
getFollowing("light-to-temperature map"),
print("generating humidity")
getFollowing("temperature-to-humidity map"),
print("generating location")
getFollowing("humidity-to-location map"),
print(tab)
minLocation = 100000000000000000000000000000
for key, value in tab.items():
    if int(value[-1]) < minLocation:
        minLocation = int(value[-1])

print(minLocation)
