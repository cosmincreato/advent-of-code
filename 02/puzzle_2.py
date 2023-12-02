sum = 0

with open("input2.txt") as file:
    for game in file:
        minCubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        s = game.split(": ")
        for rounds in s[1].split("; "):
            for cubes in rounds.split(", "):
                i = cubes.split()
                i[0] = int(i[0])
                minCubes[i[1]] = max(i[0], minCubes[i[1]])
        power = minCubes["red"] * minCubes["green"] * minCubes["blue"]
        sum += power
print(sum)