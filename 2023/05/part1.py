with open("input.txt") as file:
    seeds = [int(x) for x in file.readline()[7:].split()]
    next(file)
    for i in range(7):
        next(file)
        while True:
            line = file.readline().rstrip('\n')
            if not line:
                break
            new, start, lg = [int(x) for x in line.split()]
            for k in range(len(seeds)):
                if start <= seeds[k] < start+lg:
                    seeds[k] += new - start
    print(min(seeds))