class Solution:

    unique_code = "$"
    def encode(self, strs: List[str]) -> str:
        #  I think encode as adding all strings  
        encoded = ""     
        for word in strs:
            encoded += f"{len(word)}{self.unique_code}{word}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            count_str = ""
            while s[i] != self.unique_code:
                count_str += s[i]
                i += 1
            count = int(count_str)
            if count == 0:
                decoded.append("")
            else:
                decoded.append(s[(i+1):(i+count+1)])
            i += count + 1

        return decoded