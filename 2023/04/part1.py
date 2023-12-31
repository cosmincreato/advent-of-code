s = 0

with open("input.txt") as file:
    for card in file:
        pts = 0
        numbers = card.split(": ")[1].strip().split(" | ")
        for win in numbers[0].split():
            for mine in numbers[1].split():
                if win == mine:
                    if pts == 0:
                        pts = 1
                    else:
                        pts *= 2
        s += pts
print(s)
