class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_dict = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}  #IIV   i=1, j=2 

        j=len(s)-1
        i=len(s)-2
        sum=roman_dict[s[j]]
        while(i>=0):
            right=s[j]
            left=s[i]
            if(roman_dict[left]>=roman_dict[right]):
                sum+=roman_dict[left]
            else:
                sum-=roman_dict[left]
            i-=1
            j-=1
        return sum