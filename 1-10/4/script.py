f = open("./input.txt", "r")
sum = 0
copies = {}
game = 0
for i in f:
    game+=1
    if game not in copies:
        copies[game] = 0
    copies[game] = copies[game] +1
    cardValue = 0
    card = i.split(':')[1].split("|")[0].split(" ")
    while '' in card:
        card.remove('')
    myCard = i.split(':')[1].split("|")[1][0:-1].split(" ")
    while '' in myCard:
        myCard.remove('')
    for j in card:
        if j in myCard:
            cardValue += 1
    for g in range(1, cardValue+1):
        if game+g not in copies:
            copies[game+g] = 0
        copies[game+g] = copies[game+g] + copies[game]
for i in copies:
    sum += copies[i]
print(sum)
