function isPrime(num){
    var prime=false;
    for(var i=2; i<num; ++i){
        if(num%i==0){
            return num+" is divisible by "+i+ " ";
            prime=false;
        }
        else prime=true;
    }
    return prime;
}
