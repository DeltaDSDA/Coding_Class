n = int(input())
cnt = 0
while a != 0:
    if a % 2 == 1:
        cnt += 1
    n = n // 2
print(cnt)
