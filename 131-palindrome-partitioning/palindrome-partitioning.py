class Solution:
    def isPalindromic(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    def findAllPalindromic(self,index, s, result, path):
        if index == len(s):
            result.append(path[:])
            return 
        for i in range(index, len(s)):
            if self.isPalindromic(s, index, i):
                path.append(s[index:i+1])
                self.findAllPalindromic(i+1, s, result, path)
                path.pop()
    

    
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        index = 0
        self.findAllPalindromic(index, s, result, path)
        return result

        