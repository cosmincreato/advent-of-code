def step(line):
    for i in range(len(line) - 1):
        line[i] = line[i + 1] - line[i]
    line.pop(-1)
    return line


with open("input.txt") as file:
    ans = 0
    lines = [[int(x) for x in line.rstrip('\n').split()] for line in file]
    for line in lines:
        while not all(x == 0 for x in line):
            ans += line[-1]
            line = step(line)

print(ans)
