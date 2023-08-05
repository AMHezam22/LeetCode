class Solution:
    def findLong(self,text):
        s = set()
        long = 0
        for x in text:
            if x in s:
                return len(s)
            else:
                s.add(x)
        return len(s)
    def lengthOfLongestSubstring(self, text: str) -> int:
        i = 0
        longest = 0
        while i<len(text)-longest:
            longest = max(longest,self.findLong(text[i:]))
            i += 1
        return longest