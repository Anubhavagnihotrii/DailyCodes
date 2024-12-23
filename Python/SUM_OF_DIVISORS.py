def sumOfDivisors( n):
    	#code here 
	sum=0
	for i in range(1,n+1):
		divisor=n//i
		sum+=divisor*i
	return sum

sumOfDivisors(12)