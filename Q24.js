
// num=[13,45,67,89,56,44,56,34]
// i=num.length-1
// list=[]
// while(i>=0){
//     n=num[i]
//     list.push(n)
//     i=i-1
// }console.log(list)
a=[[2,3,4],5,[3,6,5],6,[2,5,6,7],7,9]

sum=0
for (i of a){
    n=i
    // console.log(typeof(n))
    if (typeof(n)==="object"){
        // console.log(typeof(n))
        for (j of n){
            sum=sum+j
            
        }
    }else{
        sum=sum+i
    }
    
    
}console.log(sum)