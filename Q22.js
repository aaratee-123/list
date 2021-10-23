mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
// # subStr = "over"
// # replacementStr = "on" 
// l=mainStr.split()
// i=0
// x=mainStr.replace("over", "on")
// while i<len(l):
//     if l[i]=="over":
//         x=mainStr.replace("over", "on")
//         #continue
//     i=i+1
// print(x)
var Substr="over"
var replacementStr=" "
var l=mainStr.split(" ")
x=mainStr.replace("over","on")
for (i of l){
    // replacementStr=replacementStr+i+" "
    x=mainStr.replace("over", "on")
    
} console.log(x)

