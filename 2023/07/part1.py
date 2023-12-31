STRENGTH_ORDER = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')


def hand_type(hand):
    count = {}
    for card in hand:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1
    sorted_values = sorted(count.values(), reverse=True)
    if len(sorted_values)==1:
        sorted_values.append(0)
    return sorted_values[:2]


def card_compare(hand1, hand2):
    i = 0
    while hand1[i] == hand2[i]:
        i += 1
    if STRENGTH_ORDER.index(hand1[i]) > STRENGTH_ORDER.index(hand2[i]):
        return 1
    else:
        return 0


with open("input.txt") as file:
    hands = [x.rstrip('\n').split() for x in file.readlines()]
    ranks = [1 for x in range(len(hands))]
    ans = 0

    for i in range(len(hands)):
        hand_i, bid_i = hands[i]
        for j in range(i + 1, len(hands)):
            hand_j, bid_j = hands[j]
            max1_i, max2_i = hand_type(hand_i)
            max1_j, max2_j = hand_type(hand_j)
            if max1_i > max1_j or (max1_i == max1_j and max2_i > max2_j):
                ranks[i] += 1
            elif max1_i == max1_j and max2_i == max2_j:
                if card_compare(hand_i, hand_j):
                    ranks[j] += 1
                else:
                    ranks[i] += 1
            else:
                ranks[j] += 1

for i in range(len(hands)):
    bid = int(hands[i][1])
    rank = ranks[i]
    ans += bid * rank

print(ans)