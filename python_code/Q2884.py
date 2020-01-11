h,m=map(int, input().split())
if h==0:
    h=24
if m>=45:
    print("%d, %d", h, m-45)
else:
    print("%d, %d", h-1, (60+m)-45)
