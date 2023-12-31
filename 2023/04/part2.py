s = 0
amount = {}

with open("input.txt") as file:
    for card in file:
        sp = card.split(": ")
        cardId = int(sp[0].split()[1])
        numbers = sp[1].strip().split(" | ")
        count = cardId
        amount[count] = amount.get(count, 1)
        for win in numbers[0].split():
            for mine in numbers[1].split():
                if win == mine:
                    count += 1
                    amount[count] = amount.get(count, 1)
                    amount[count] += amount[cardId]
        s += amount[cardId]
print(s)
