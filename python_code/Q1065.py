a = int(input())
h = 0

for n in range(1, a+1) :
    if n <= 99 :
        h += 1 
    
    else :     
        b = list(map(int, str(n))) 
        if b[0] - b[1] == b[1] - b[2] :
            h+=1
print(h)   
