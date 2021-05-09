marks=[[78,76,94,86,88],[91,71,98,65],[95,45,78,],[87,67,49,68,88]]
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
    while j<4:
        m=marks[1][j]
        ad=ad+m
        print(ad)
        j=j+1
    k=0
    addition=0
    while k< 3:
        n=marks[2][k]
        addition=addition+n
        print(addition)
        k=k+1
    p=0
    addi=0
    while p<5:
        l=marks[3][p]
        addi=addi+l
        print(addi)
        p=p+1
    i=i+1
sum=(add+ad+addition+addi)
print(sum)

