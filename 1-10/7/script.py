f = open("./input.txt", "r")
table = []
# 251275185
cardOrder = "AKQT98765432J"


def hand1IsBetter(hand1, hand2):
    if hand1[2] < hand2[2]:
        return False
    elif hand1[2] > hand2[2]:
        return True
    else:
        if len(hand1[0]) != 5:
            print(hand1 + " " + str(len(hand1[0])))
        i = 0
        while hand1[0][i] == hand2[0][i] and i < 4:
            i += 1
        if cardOrder.index(hand1[0][i]) < cardOrder.index(hand2[0][i]):
            return True
        return False


def getStatus(hand):
    if isFiveOfKind(hand):
        return 7
    elif isForOfKind(hand):
        return 6
    elif isFullHouse(hand):
        return 5
    elif isThreeOfKind(hand):
        return 4
    elif isTwoPair(hand):
        return 3
    elif isOnePair(hand):
        return 2
    elif isHighCard(hand):
        return 1
    else:
        return 0


def isFiveOfKind(hand):
    for i in hand:
        if hand.count(i) == 5 or (hand.count(i) + hand.count('J') == 5 and i != 'J'):
            return True
    return False


def isForOfKind(hand):
    for i in hand:
        if hand.count(i) == 4 or (hand.count(i) + hand.count('J') == 4 and i != 'J'):
            return True
    return False


def isFullHouse(hand):
    diff = {}
    for i in hand:
        if i != 'J':
            diff[i] = hand.count(i)
    if len(diff) > 2:
        return False
    return True


def isThreeOfKind(hand):
    for i in hand:
        if hand.count(i) == 3 or (hand.count(i) + hand.count('J') == 3 and i != 'J'):
            return True
    return False


def isTwoPair(hand):
    previous = ""
    for i in hand:
        if hand.count(i) == 2 and i != previous and previous != "":
            return True
        elif hand.count(i) == 2 and previous == "":
            previous = i
    return False


def isOnePair(hand):
    for i in hand:
        if hand.count(i) == 2 or (hand.count(i) + hand.count('J') == 2 and i != 'J'):
            return True
    return False


def isHighCard(hand):
    for i in hand:
        if hand.count(i) != 1:
            return False
    return True


for i in f:
    table.append((i.split(" ")[0], i.split(" ")[1][:-1], -1))

for i in range(len(table)):
    table[i] = (table[i][0], table[i][1], getStatus(table[i][0]))

sortTable = []

for i in range(len(table)):
    max = table[0]
    for j in range(len(table)):
        if hand1IsBetter(table[j], max):
            max = table[j]
    sortTable.append(max)
    table.remove(max)

sum = 0
for i in range(len(sortTable)):
    sum += int(sortTable[i][1]) * (len(sortTable) - i)

print(sortTable)
print(sum)
