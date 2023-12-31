with open("input.txt") as file:
    time = [int(x) for x in file.readline()[5:].split()]
    score = [int(x) for x in file.readline()[9:].split()]
    ans = 1
    for i in range(len(time)):
        p = 0
        for j in range(1,time[i]):
            if j * (time[i] - j) > score[i]:
                p += 1
        ans *= p
    print(ans)