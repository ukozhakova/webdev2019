// make an array of four numbers
var myFirstArray = [293, 103, 499, 288];

// display the element at index 2 (aka the 3rd element)
fill(0, 0, 0);
text(myFirstArray[2], 100, 100);

// make a bigger array that holds the height of each bar
var bars = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100];

// draw a bar for each element in the array
for (var i = 0; i < bars.length; i += 1) {
    var x = i * 35 + 15;
    var bar = bars[i];
    rect(x, 200, 20, bar);
}