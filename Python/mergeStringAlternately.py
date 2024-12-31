class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # return ''.join(a+b for a,b in zip_longest(word1,word2,fillvalue=''))
        newstr=''
        i=0
        while i<=len(word1)-1 and i<=len(word2)-1:
            newstr=newstr+ word1[i] +word2[i]
            i+=1
        if i<=len(word1)-1:
            while i<=len(word1)-1:
                newstr+=word1[i]
                i+=1
        else:
            while i<=len(word2)-1:
                newstr+=word2[i]
                i+=1
        return newstr
            
        