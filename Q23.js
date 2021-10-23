a=[40,30,50,60,10]
i=0
while (i< a.lenght){
    j=i+1
    while (j<i){
        i=a[j]
        console.log(i,a[j])
        j=j+1
    }i=i+1
}a.sort()
console.log(a)