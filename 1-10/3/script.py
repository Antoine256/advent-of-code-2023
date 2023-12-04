def isSymbolAround(tab, index1, first, last):
    for i in range(index1 - 1, index1 + 2):
        if i < 0 or i >= len(tab):
            continue
        for j in range(first - 1, last + 2):
            if j < 0 or j >= len(tab[i]):
                continue
            if tab[i][j] in "+-*/?;,:/|\\=()[]{}<>!@#$%^&*~`'\"":
                if tab[i][j] == '*':
                    for k in range(j - 1, j + 2):
                        if k < 0 or k >= len(tab[i]):
                            continue
                        for l in range(i - 1, i + 2):
                            print("on cherche : " + tab[l][k])
                            if l < 0 or l >= len(tab):
                                continue
                            if tab[l][k].isdigit() and (l != index1 or not (first <= k <= last)) and l >=index1 and (k >= j or l != index1):
                                number = [tab[l][k]]
                                ktemp = k+1
                                while tab[l][ktemp].isdigit():
                                    number.append(tab[l][ktemp])
                                    ktemp += 1
                                ktemp = k-1
                                while tab[l][ktemp].isdigit():
                                    number.insert(0, tab[l][ktemp])
                                    ktemp -= 1
                                num = "".join([str(m) for m in number])
                                print(tab[index1][first:last + 1] + " * " + num)
                                return (int(tab[index1][first:last + 1]) * int(num))
                # return int(tab[index1][first:last + 1])
    return -1


f = open("./input.txt", "r")
sum = 0
tab = []
for i in f:
    tab.append(i)
for i in range(len(tab)):
    # if i > 0:
    #     print(tab[i - 1])
    # print(tab[i])
    # if i < len(tab) - 1:
    #     print(tab[i + 1])
    #     if i < len(tab) - 2:
    #         print(tab[i + 2])
    j = 0
    while j < len(tab[i]) - 1:
        if tab[i][j].isdigit():
            first = j
            while tab[i][j].isdigit():
                j += 1
            last = j - 1
            print("on traite : " + tab[i][first:last + 1])
            res = isSymbolAround(tab, i, first, last)
            if res != -1:
                print("good résult : "+str(res))
                sum += res
        j += 1
print(sum)
# 1 : 521515
# 2 : 53894126
