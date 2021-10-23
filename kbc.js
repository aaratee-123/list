var question_list = [
    "How many continents are there?",              //pehla question
    "What is the capital of India?",            //doosra question
    "NG mei kaun se course padhaya jaata hai?",    // teesra question
    "what is longest river in india?"       //fourth question
]
var options_list = [
    //pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    //second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    //third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],
    ["Bramhaputra","Ganga","Narmada","Godavari"]
]
// har ek question ke liye, uski solution key (yeh index nahi hai)

var solution_list = [3, 4, 1,2] 
var answer_list=[
    ["(1)four","(3)seven"],
    ["(2)Bhopal","(4)Delhi"],
    ["(1)Software Engineering","(4)Agriculture"],
    ["(2)Ganga","(3)Narmada"]
]
console.log("KON BANEGA COROREPATI***")
var num=require("readline-sync")
var i=0;
var s=0;
var count=0;
while(i<question_list.length){
    console.log(question_list[i])
    var a=0;
    var b=i;
    while(a<options_list[i].length){
        var k=options_list[b][a]
        console.log(a+1,k)
        a=a+1
    }num1=num.question("do you want 50 50 lifeline(y/n)")
    if (num1=="y"){
        console.log("50 50 lifeline")
        if (count<1){
            console.log(answer_list[b])
            num2=num.questionInt("enter your answer")
            if (num2==solution_list[i]){
                s+=10000
                console.log("your answer is correct")
                console.log("you win Rs/",s)
                count+=1
            }else{
                console.log("incorrect answer")
                console.log("you can,t play again")
                console.log("you win Rs/",s)
                console.log("\U0001F629")
                count+=1
                break
            }

        }else{
            console.log("you already use lifeline :")
            m=num.questionInt("enter your answer :")
            if (m==solution_list[i]){
                console.log("congrats your answer is right")
                s+=10000
                console.log("you win Rs/",s)
            }else{
                console.log("No chance")
                console.log("youe answer is wrong")
                console.log("you win",s)
                break
            }
        }
    }else{
        var answer3=num.questionInt("enter your amswer3:")
        if(answer3==solution_list[i]){
            console.log("your anser is correct")
            s=s+10000
            console.log("you win Rs/:",s)
        }else{
            console.log("your anser is wrong ")
            console.log("you won Rs/:")
        }//i++;
    }i++

}console.log("congratulation you are a part of _KON BANEGA COROREPATI")
console.log("you win Rs/",s)
console.log("THANK YOU BEING PART OF KBC")