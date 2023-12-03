s = 0

with open("input.txt") as file:
    for game in file:
        minCubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        sp = game.split(": ")
        for rounds in sp[1].split("; "):
            for cubes in rounds.split(", "):
                i = cubes.split()
                i[0] = int(i[0])
                minCubes[i[1]] = max(i[0], minCubes[i[1]])
        power = minCubes["red"] * minCubes["green"] * minCubes["blue"]
        s += power
print(s)