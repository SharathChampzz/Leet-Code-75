class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        The GCD of two strings is the largest string that can be concatenated multiple times to form both str1 and str2.
        """
        # Check if concatenated strings are equal
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute the GCD of the lengths of str1 and str2
        gcd_length = math.gcd(len(str1), len(str2))
        
        
        # Return the prefix of str1 with length equal to gcd_length
        return str1[:gcd_length]