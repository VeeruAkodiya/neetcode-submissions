class Solution:
    def isPalindrome(self, s: str) -> bool:
        # iterate from both sides
        low = s.lower()
        char = ""
        for ch in low:
            if ("a" <= ch and "z" >= ch) or ("0" <= ch and "9" >= ch):
                char += ch
        str_len = len(char)
        i = 0
        j = str_len -1
        while i < j:
            if char[i] != char[j]:
                return False
            i += 1
            j -= 1
        return True