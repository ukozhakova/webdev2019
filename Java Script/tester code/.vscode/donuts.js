/*
 * Programming Quiz: Donuts Revisited (7-6)
 */

var donuts = [
    { type: "Jelly", cost: 1.22 },
    { type: "Chocolate", cost: 2.45 },
    { type: "Cider", cost: 1.59 },
    { type: "Boston Cream", cost: 5.99 }
];
// for(var i=0; i<donuts.length; ++i){

//         console.log(donuts[i][j].type + " is" + donuts[i][j].cost);

// }
donuts.forEach(function(donn){
    console.log(donn.type+ " donuts cost $"+donn.cost+" each");
})
// your code goes here
