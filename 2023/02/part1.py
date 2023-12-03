s = 0

with open("input.txt") as file:
    for game in file:
        possible = True
        sp = game.split(": ")
        id = sp[0][5:]
        for rounds in sp[1].split("; "):
            for cubes in rounds.split(", "):
                i = cubes.split()
                if (i[1]=="red" and int(i[0])>12) or (i[1]=="green" and int(i[0])>13) or (i[1]=="blue" and int(i[0])>14):
                    possible = False
        if possible:
            s += int(id)
print(s)