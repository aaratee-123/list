a=[1,2,[3,4],5,6,[7,8],[9],10]
i=0
while i<len(a):
    j=0
    while j<3:
        if a[i][j]==a[2][0]:
            k=a[i][j]+10
            print(k)
            k.append(a)
        print(a)
    i=i+1


        
        
    
