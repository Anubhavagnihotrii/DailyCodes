class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code 
        gcd=0
        n1=a
        n2=b
        while a>0 and b>0:
            if a>b:
                a = a%b #stores the rem in a
            else:
                b = b%a
            
            
        if a==0:
            gcd= b
        else:
             gcd= a
    
                
        Lcm= (n1*n2)//gcd
        
        return [Lcm,gcd]