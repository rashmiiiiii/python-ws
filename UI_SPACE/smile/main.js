function factorial()
{   
    num=parseInt(document.getElementById('num').value);
    message ="";
    if(num){
    res = 1;
    for(i=2;i<= num;i++)
    {
        res = res*i;
    }
    message ="factorial of"+num+"is"+res;
    document.getElementById('res').innerHTML=message;
}
else{
    document.getElementById('res').innerHTML="";
}

}
function digitsum()
{
    message = "";
    num=parseInt(document.getElementById('num').value);
    num1 = num;
    sum = 0;
    if(num)
    {
        while(num != 0){
            sum += parseInt(num%10);
            num =parseInt(num/10);
        }
        message ="sum of digits:"+sum;
        document.getElementById('res').innerHTML=message;
    }
    else{
        document.getElementById('res').innerHTML="";
    }
}
function reverse()
{
    message = "";
    num=parseInt(document.getElementById('num').value);
    num1 = num;
    rev = 0;
    if(num)
    {
        while(num != 0){
            rev =rev * 10 + parseInt(num%10);
            num =parseInt(num/10);
        }
        message ="rev of num:"+num1+ "is"+rev;
        document.getElementById('res').innerHTML=message;
    }
    else{
        document.getElementById('res').innerHTML="";
    }
}

function palindrome()
{
    message = "";
    num=parseInt(document.getElementById('num').value);
    num1 = num;
    rev = 0;
    if(num)
    {
        while(num != 0){
            rev =rev * 10 + parseInt(num%10);
            num =parseInt(num/10);
        }
        if(rev === num1){
        message = "number:"+num1+"is"+"palindrome";
        document.getElementById('res').innerHTML=message;
    }
}
    else{
        document.getElementById('res').innerHTML="";
    }
}


