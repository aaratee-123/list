a=[3,4,5,[6,7,8],9,4,10]
i=0
while i<len(a):
    j=0
    sum=0
    while j<3:
        if a[i]==3:
            t=a[i][j]
            sum=sum+t
            print(sum)
        else:
            b=a[i]
            b=b+1
            print(b)
    j=j+1
    add=t+b
    print(add)
i=i+1
