sum = 0
with open("input1.txt") as file:
    for line in file:
        digits = []
        for k,v in enumerate(line):
            if v.isdigit():
                digits.append(v)
        sum += int(digits[0]+digits[-1])
print(sum)