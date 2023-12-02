f = open("./data.txt", "r")
number = [('1','one'),('2','two'),('3','three'),('4','four'),('5','five'),('6','six'),('7','seven'),('8','eight'),('9','nine'),('0','zero')]
sum = 0
for i in f:
    first = ""
    last = ""
    for j in range(0,len(i)-1):
        nobreak = True
        for k in number:
            if i[j] == k[0]:
                first = k[0]
                nobreak = False
                break
            if k[1] in i[0:j+1]:
                first = k[0]
                nobreak = False
                break
        if not nobreak:
            break
    for j in range(len(i)-1, -1, -1):
        nobreak = True
        for k in number:
            if i[j] == k[0]:
                last = k[0]
                nobreak = False
                break
            if k[1] in i[j-1:len(i)-1]:
                last = k[0]
                nobreak = False
                break
        if not nobreak:
            break
    sum += int(first + last)
print(sum)
f.close()
