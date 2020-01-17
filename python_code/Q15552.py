inport sys
N=sys.stdin.readline()

for Repeat in range(0, int(N)):
    num=sys.stdin.readline().split()
    print(int(num[0]) + int(num[1]))



