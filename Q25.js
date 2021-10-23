a=[[2,3,4,7],6,67,[4,5,6],4,7,[5,6,7],5,12,[8,9,10]]
// sum=0
// for (i of a){
//     for (j of i){
//         sum=sum+j
//     }
// }console.log(sum)
for (i in a){
    b=a[i]
    if (typeof(b)=="object"){
        for(j in b ){mmmmmm
            c=b[j]
            if(c%2==0){
                console.log(c,"even")
            }
            else{
                console.log(c,"odd");
            }
        }
    }
    else{
        if(b%2==0){
            console.log(b,"even");
        }
        else{
            console.log(b,"odd");
        }
    }
}