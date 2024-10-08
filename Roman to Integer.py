s = "MCMXCIV"

pairs = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
individual = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

value = 0
head = len(s) - 2
tail = len(s)
# print(head, tail)
# print(s[head:tail])

while tail != 0:
    print(s[head:tail])
    if s[head:tail] in pairs.keys():
        value += pairs[s[head:tail]]
        print("Yes")
        tail -= 2
        head -= 2

    else:
        head += 1
        value += individual[s[head:tail]]
        head -= 2
        tail -= 1
print(value)