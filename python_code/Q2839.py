sugar = int(input())
n = 0

while sugar > 0:
    if sugar % 5 != 0:
        sugar -= 3
        if sugar < 0:
            n = -1
            break
        n += 1
    elif sugar % 5 == 0:
        n += 1
        sugar -= 5
    elif sugar % 5 != 0 and sugar % 3 != 0:
        n = -1

print(n)
