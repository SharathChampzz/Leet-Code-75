class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer, t_pointer = 0, 0
        s_len, t_len = len(s), len(t)

        while s_pointer < s_len and t_pointer < t_len:
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1

            t_pointer += 1

        return s_pointer == s_len