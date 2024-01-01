with open("input.txt") as file:
    nodes = {}
    steps = file.readline().rstrip('\n')
    next(file)
    for line in file:
        line = line.split()
        line.pop(1)
        line = [x.strip("(),") for x in line]
        pos, left, right = line
        nodes[pos] = tuple([left, right])

steps_lg = len(steps)
pos = 'AAA'
i = 0

while pos != 'ZZZ':
    step = steps[i % steps_lg]
    crt = 1 if step == 'R' else 0
    pos = nodes[pos][crt]
    i += 1
print(i)