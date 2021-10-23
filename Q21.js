var n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
list=[]
duplicates=[]
for (i of n){
    if (!list.includes(i)){
        list.push(i)
    }
}console.log(list)


for(var j of list){
    count=0
    for(var k of n){
        if (j === k){
            count+=1
        }
    }if(count >1){
        duplicates.push(j);
    };
}console.log(duplicates);
