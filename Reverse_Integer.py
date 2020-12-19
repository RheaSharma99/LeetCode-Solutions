# Question Name: Reverse Integer
# Difficuly level: EASY

# Question prompt: 
    # Given a 32-bit signed integer, reverse digits of an integer.
    # Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# Question Intuition: 
    # given a negative integer solve for modulus integer and add negative sign.
    # as long as the number isn't 0 you divide it by 10 to get the digit at the end
    # you successively multiply by 10 and add the remainder to create the reversed number.
    # add the size constraint.

# SOLUTION 1:

class Solution:
    def reverse(self, x: int) -> int: # x = 1234
        rev = 0
        is_neg = x < 0
        if is_neg:
            x = -x
            
        while(x != 0):
            a = x % 10 #4 #3 #2 #1 
            rev = rev * 10 + a #4 #4*10 + 3 # (4 * 10 + 3)* 10 + 2 ...
            x = (x - a) / 10 #123 #12 #1 
         
        factor = -1 if is_neg else 1
        
        ans = (factor * int(rev))
        
        if -math.pow(2,31) <= ans <= math.pow(2,31) - 1:
            return ans
        else:
            return 0