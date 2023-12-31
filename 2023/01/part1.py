s = 0
with open("input.txt") as file:
    for line in file:
        digits = []
        for k,v in enumerate(line):
            if v.isdigit():
                digits.append(v)
        s += int(digits[0]+digits[-1])
print(s)

