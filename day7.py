from operator import itemgetter

file = open("input.txt", 'r')
# file = open("input_test.txt", 'r')

lines = [line.split() for line in file]

power_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '': 0}

players = list()
for line in lines:
    hand = line[0]
    bid = int(line[1])
    # temp_most_common = 0
    # temp_common = ''
    # if 'J' in hand:
    #     for card in set(hand):
    #         if hand.count(card) >= temp_most_common:
    #             temp_common = hand.count(card)

    strength = hand.count(max(set(hand), key = hand.count))
    if strength == 2:
        temp = 0
        for card in set(hand):
            if hand.count(card) == 2:
                temp += 1
        if temp == 2:
            strength = 2.5

    if strength == 3:
        temp = 0
        for card in set(hand):
            if hand.count(card) == 2:
                temp += 1
        if temp == 1:
            strength = 3.5
    
    second_order = list() 
    for card in hand:
        second_order.append(power_dict[card])
    players.append([hand, bid, strength, second_order])

players = sorted(players, key=itemgetter(2))

def find_winnings(players):
    result = 0
    temp_strength = 1
    ranges = list()
    ranges.append(0)
    for i in range(len(players)):
        if players[i][2] > temp_strength:
            temp_strength = players[i][2]
            ranges.append(i)
    ranges.append(len(players))
    for i in range(len(ranges)-1):
        players[ranges[i]:ranges[i+1]] = sorted(players[ranges[i]:ranges[i+1]], key=itemgetter(3))

    for i in range(len(players)):
        result += (i + 1) * players[i][1]

    return result

result = find_winnings(players)
print(result)