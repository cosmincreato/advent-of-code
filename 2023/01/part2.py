s = 0
d = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
with open("input.txt") as file:
    for line in file:
        digits = []
        for k,v in enumerate(line):
            if v.isdigit():
                digits.append(v)
            for i, j in enumerate(d):
                if line[k:].startswith(j):
                    digits.append(str(i + 1))
        s += int(digits[0]+digits[-1])
print(s)