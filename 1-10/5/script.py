f = open("./input.txt", "r")
data = {}
title = ""
for i in f:
    if i.split(':')[0] == "seeds":
        data["seeds"] = i.split(':')[1].split(" ")[1:]
        data["seeds"][-1] = data["seeds"][-1][:-1]
    elif not i[0].isdigit():
        title = i[0:-2]
        data[title] = []
    elif i[0].isdigit():
        data[title].append(i[0:-1].split(" "))
f.close()
tab = {}
for i in data["seeds"]:
    tab[i] = [i]


def getFollowing(next, fe):
    # destination source range
    for key, value in tab.items():
        gotValue = False
        for j in data[next]:
            print(str(j[1])+" "+ str(int(j[1])+int(j[2]))+ "contains" +str(value[-1]))
            if int(j[1])< int(value[-1]) < int(j[1])+int(j[2]):
                tab[key].append(int(value[-1])+int(j[0])-int(j[1]))
                gotValue = True
                break
        if not gotValue:
            tab[key].append(value[-1])

print("generating seeds")
getFollowing("seed-to-soil map", "seeds"),
print("generating fertilizer")
getFollowing("soil-to-fertilizer map", "seed-to-soil map"),
print("generating water")
getFollowing("fertilizer-to-water map", "soil-to-fertilizer map"),
print("generating light")
getFollowing("water-to-light map", "fertilizer-to-water map"),
print("generating temperature")
getFollowing("light-to-temperature map", "water-to-light map"),
print("generating humidity")
getFollowing("temperature-to-humidity map", "light-to-temperature map"),
print("generating location")
getFollowing("humidity-to-location map", "temperature-to-humidity map"),
print(tab)
minLocation = 100000000000000000000000000000
for key, value in tab.items():
    if int(value[-1]) < minLocation:
        minLocation = int(value[-1])

print(minLocation)
