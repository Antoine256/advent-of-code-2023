f = open("./input.txt", "r")
data = {}
instruction = []
for i in f:
    if i.__contains__("="):
        i = i.strip()
        key = i.split("=")[0].replace(" ", "")
        data[key] = i.split("=")[1].split(" ")[1:]
        for k in range(0, len(data[key])):
            data[key][k] = data[key][k].replace("(", "")
            data[key][k] = data[key][k].replace(")", "")
            data[key][k] = data[key][k].replace(",", "")
    else:
        for j in i:
            if j != "" and j != "\n":
                instruction.append(j)
print(data)
print(instruction)

nodes = []
for key in data.keys():
    if key[-1] == 'A':
        nodes.append(key)
print("nodes : " + str(nodes))
cpt = 0


def allNodeFinishedByZ():
    for i in nodes:
        if i[-1] != "Z":
            return False
    return True

lennodes = len(nodes)

while not allNodeFinishedByZ():
    for i in instruction:
        cpt += 1
        for j in range(0,len(nodes)):
            if i == "L":
                nodes[j] = data[nodes[j]][0]
            elif i == "R":
                nodes[j] = data[nodes[j]][1]
print(cpt)
