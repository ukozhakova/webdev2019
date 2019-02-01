/*
 * Programming Quiz: Laugh (5-4)
 */

var laugh = function(number){
    var str="";
    for(var i=0; i<number; ++i){
        str+="ha";
    } str+="!";
    return str;
}

console.log(laugh(10));
