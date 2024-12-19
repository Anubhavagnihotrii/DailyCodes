import java.util.*;
class CountDigit {
    public static void main(String[] args) {
        int n =1111;
        int rem=0;
        int num =n;
        HashSet<Integer> set = new HashSet<>();
        while(n>0){
            rem=n%10;
            if(rem==0){
                n=n/10;
                continue;
            }
            if(num%rem==0){
                set.add(rem);
            }
            n=n/10;
        }
        // System.out.println(count);
        System.out.println(set.size());
    }
}