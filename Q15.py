marks=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
i=0
while i <1:
    b=0
    add=0
    while b<5:
        l=marks[0][b]
        add=add+l
        print(add)
        b=b+1
    j=0
    ad=0
    while j<5:
        m=marks[1][j]
        ad=ad+m
        print(ad)
        j=j+1
    k=0
    addition=0
    while k< 5:
        n=marks[2][k]
        addition=addition+n
        print(addition)
        k=k+1
    i=i+1
sum=(add+ad+addition)
print(sum)

