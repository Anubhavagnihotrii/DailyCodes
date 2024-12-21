public class LcmAndGcd{
    public static void main(String[] args) {
        int a=10;
        int b=20;
        int m=a;
        int n=b;
        int gcd=1;
        while(a>0 && b>0){
            if(a>b){
                a=a%b;
            }
            else{
                b=b%a;
            }
        }
        if(a==0){
            gcd=b;
        }else{
            gcd=a;
        }
        int lcm = (m*n)/gcd;
        
        System.out.println(lcm+" "+gcd);
        
    }
}