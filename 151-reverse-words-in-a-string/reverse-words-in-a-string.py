class Solution:
    def reverseWords(self, s: str) -> str:
        # Trim leading and trailing spaces
        s = s.strip()
        
        # Split the string into words
        words = s.split()
        
        # Reverse the list of words
        words.reverse()
        
        # Join the words with a single space
        return ' '.join(words)
        