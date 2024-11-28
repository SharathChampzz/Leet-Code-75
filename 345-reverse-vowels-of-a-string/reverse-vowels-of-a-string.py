class Solution:
    def reverseVowels(self, s: str) -> str:
        left_p = 0
        right_p = len(s) - 1
        s = list(s) # we cannot do implace replace for strings

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} # for faster lookup using set()

        while left_p < right_p:
            if s[left_p] not in vowels:
                left_p += 1
            elif s[right_p] not in vowels:
                right_p -= 1
            else:
                temp = s[left_p] # swap
                s[left_p] = s[right_p]
                s[right_p] = temp

                left_p += 1
                right_p -= 1

        return ''.join(s)
            
        