class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)

        result_str = ""
        i, j = 0, 0

        # iterate through both the strings
        while (i < len1) and (j < len2):
            result_str += word1[i]
            result_str += word2[j]
            
            i += 1
            j += 1

        # if there is character left in first string
        while i < len1:
            result_str += word1[i]
            i += 1

        # if there is character left in second string
        while j < len2:
            result_str += word2[j]
            j += 1

        """
        # or Append the remaining characters like below
        result_str += word1[i:] # sliciing doesnot raise exception for out of range, it handles it
        result_str += word2[j:]
        """

        return result_str

            
        