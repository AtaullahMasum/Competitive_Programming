class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        length = len(s)
        for i in range(length):
            if s[i] == '1':
                count +=1 
        return ('1'*(count-1)) +('0'*(length-count))+'1'
        