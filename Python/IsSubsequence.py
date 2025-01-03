class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_ptr, t_ptr = 0, 0

        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1  # Move the pointer in `s` only if there's a match
            t_ptr += 1  # Always move the pointer in `t`

        return s_ptr == len(s)