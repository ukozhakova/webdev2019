/*
 * Programming Quiz: JuliaJames (4-1)
 */

var x = 1;

while (x<=20) {
    if(x%15===0){
        console.log("JuliaJames");
        x++;
        
    }else if(x%5===0){
        console.log("James");
        x++;
        
    }
    else if(x%3===0){
        console.log("Julia");
        x++;
        
    }
    else {console.log(x);
    x=x+1;
    
    }
    // check divisibility
    // print Julia, James, or JuliaJames
    // increment x
}
