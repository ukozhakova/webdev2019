//today's date at the top Corner
n= new Date();
y=n.getFullYear();
m=n.getMonth()+1;
d=n.getDate();
document.getElementById("date").innerHTML=d+"/"+"0"+m+"/"+y;

//greeting
var text;
var userName=prompt("Please enter your name","Ulbo");
if(userName===null || userName===""){
    userName="User";
}
else{
    text="Hello, "+ userName+" ! What is your main focus for today?";
}
document.getElementById("greeting").innerHTML=text;


//Main Part

var myList = document.getElementsByTagName("li"); //for each list in ul creating close btn
for (var i = 0; i < myList.length; i++) {
  var span = document.createElement("span"); //creating span for close element
  var txt = document.createTextNode("\u00D7"); //code of x
  span.className = "close"; //for css
  span.appendChild(txt); //привязываем x to span
  myList[i].appendChild(span);//privyazivaem span to list
}

//deleting elem from TODO list
var close = document.getElementsByClassName("close"); //getting all elem-s with class close
for (var i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement; //parent of close elem is list element
    div.style.display = "none"; //invisible
  }
}

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') { //on click it will marked as checked
    ev.target.classList.toggle('checked'); //class will be checked
  }
}, false);

// Create a new list item when clicking on the "Add" button
function newElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("myInput").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("You cannot add empty task. Please, write something!");
  } else {
    document.getElementById("myUL").appendChild(li);
  }
  document.getElementById("myInput").value = "";

  var span = document.createElement("SPAN");//creating elem with type span
  var txt = document.createTextNode("\u00D7");//for new added elems
  span.className = "close"; 
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}