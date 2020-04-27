#!/usr/bin/env python3
#####################################
# EXAMPLE:  testing for palindromes
#####################################

def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
                print(ans, end =" ")
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

#print(isPalindrome('eve'))
print(isPalindrome('Able was I, ere I saw Elba'))
