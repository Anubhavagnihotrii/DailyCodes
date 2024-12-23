public class SumOfDivisors {
    public static void main(String[] args) {
        int n =4;
        int sum =0;
        for(int i=1;i<=n;i++){
            int divisor = n/i;
            sum+= divisor*i;
        }
        System.out.println("Sum of divisors is "+sum);
    }
}


// Input: n = 4
// Output: 15
// Explanation:
// F(1) = 1
// F(2) = 1 + 2 = 3
// F(3) = 1 + 3 = 4
// F(4) = 1 + 2 + 4 = 7
// So, F(1) + F(2) + F(3) + F(4)
//     = 1 + 3 + 4 + 7 = 15