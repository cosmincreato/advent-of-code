import math

with open("input.txt") as file:
    nodes = {}
    pos = []
    steps = file.readline().rstrip('\n')
    next(file)
    for line in file:
        line = line.split()
        line.pop(1)
        line = [x.strip("(),") for x in line]
        crtPos, left, right = line
        nodes[crtPos] = tuple([left, right])
        if crtPos[-1] == 'A':
            pos.append(crtPos)

ans = 1
steps_lg = len(steps)

for j in range(len(pos)):
    i = 0
    while pos[j][-1] != 'Z':
        step = steps[i % steps_lg]
        crt = 1 if step == 'R' else 0
        pos[j] = nodes[pos[j]][crt]
        i += 1
    ans = math.lcm(ans, i)
print(ans)
