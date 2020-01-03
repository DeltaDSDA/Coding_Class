N=int(input())
A=[]
B=[]
for i in range(N):
    A.append(int(input()))
for i in range(N):
    B.append(int(input()))

S=0
A.sort()
B.sort(reverse=True)
for i in range(N):
    S=S+A[i]*B[i]

print(S)
    
