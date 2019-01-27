/*
 * Programming Quiz: Inline Functions (5-6)
 */

// don't change this code
function emotions(myString, myFunc) {
    console.log("I am " + myString + ", " + myFunc(2));
}

// your code goes here
emotions("happy", function laugh(num){
    var str="";
    for(var i=0; i<num; ++i){
        str+="ha";
    } str+="!"; 
    return str;
})
// call the emotions function here and pass in an
// inline function expression
