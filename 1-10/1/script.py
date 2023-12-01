#52974
#53340
f = open("./data.txt", "r")
number = [('1','one', 3),('2','two', 3),('3','three', 5),('4','four', 4),('5','five', 4),('6','six', 3),('7','seven', 5),('8','eight', 5),('9','nine', 4),('0','zero', 4)]
sum = 0
for i in f:
    first = ""
    last = ""
    for j in range(0,len(i)-1):
        nobreak = True
        for k in number:
            if i[j] == k[0]: #on a un chiffre
                first = k[0]
                nobreak = False
                break
            if k[1] in i[0:j+1]: #on a un chiffre en lettre
                first = k[0]
                nobreak = False
                break
        if not nobreak:
            break
    for j in range(len(i)-1, -1, -1):
        nobreak = True
        for k in number:
            if i[j] == k[0]: #on a un chiffre
                last = k[0]
                nobreak = False
                break
            if k[1] in i[j-1:len(i)-1]: #on a un chiffre en lettre
                last = k[0]
                nobreak = False
                break
        if not nobreak:
            break
    sum += int(first + last)
print(sum)
f.close()
