def step(line):
    for i in range(len(line) - 1):
        line[i] = line[i + 1] - line[i]
    line.pop(-1)
    return line


with open("input.txt") as file:
    ans = 0
    lines = [[int(x) for x in line.rstrip('\n').split()] for line in file]
    for line in lines:
        s = line[0]
        i = 1
        while not all(x == 0 for x in line):
            line = step(line)
            s += line[0] * (-1)**(i%2)
            i += 1
        ans += s
print(ans)
