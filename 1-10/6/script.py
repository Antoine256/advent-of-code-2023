f = open("./input.txt", "r")
data = {}
for i in f:
    data[i.split(":")[0]] = i.split(":")[1][:-1].split(" ")
    while '' in data[i.split(":")[0]]:
        data[i.split(":")[0]].remove('')
f.close()
print(data)
# res = 1
# for i in range(len(data["Time"])):
#     sum = 0
#     print(int(data["Time"][i]))
#     for j in range(int(data["Time"][i])):
#         if j*(int(data["Time"][i])-j) > int(data["Distance"][i]):
#             sum += int(data["Time"][i])-2*j +1
#             break
#     print(sum)
#     print("-----")
#     res *= sum
# print(res)

nbMillisecondes = ""
bestTime = ""
for i in range(len(data["Time"])):
    nbMillisecondes += data["Time"][i]
    bestTime += data["Distance"][i]
print(nbMillisecondes)
print(bestTime)
sum = 0
nbMillisecondes = int(nbMillisecondes)
bestTime = int(bestTime)
for j in range(nbMillisecondes):
    if j*(nbMillisecondes-j) > bestTime:
        sum += nbMillisecondes-2*j +1
        break
print(sum)
