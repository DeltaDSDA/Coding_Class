a=int(input())
b=int(input())
print("%d\n%d\n%d\n%d"%((a*(b%10)),(a*((b%100)//10)),(a*(b//100)),(a*b)))
