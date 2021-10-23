// a=[1,3,6,7,13,10,12]
// i=0
// print(a)
// while i<len(a):
//     j=0
//     while j<len(a):
//         if a[i]<a[j]:
//             temp=a[i]
//             a[i]=a[j]
//             a[j]=temp
//         j=j+1
//     i=i+1
// print(a)
// b=[]
// i=1
// while i<=len(a):
//     b.append(a[-i])
//     i+=1
// print(b)


a=[1,3,5,7,8,6,13,10,12]
i=0
while (i<a.length){
    j=0
    while(j<a.length){
        if (a[i]<a[j]){
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        }
        j++
    }
    i=i+1
}console.log(a)
b=[]
i=a.length-1
while (i>=0){
    b.push(a[i])
    i--
}console.log(b)