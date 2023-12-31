with open("input.txt") as file:
    time = int(file.readline()[5:].replace(" ", "").rstrip("\n"))
    score = int(file.readline()[9:].replace(" ", "").rstrip("\n"))
    ans = 0
    for i in range(time):
        if i * (time - i) > score:
            ans = time + 1 - 2 * i
            break
    print(ans)