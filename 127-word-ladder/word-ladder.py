class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = [(beginWord, 1)]
        Set = set(wordList)
        if endWord not in Set:
            return 0
        while queue :
            word, level = queue.pop(0)
            if word == endWord:
                return level
            for i in range(len(word)):
                for  j in range(26):
                    char =  chr(ord('a')+j)
                    newWord = word[:i] + char + word[i+1:]
                    if newWord in Set:
                        queue.append((newWord,level+1))
                        Set.remove(newWord)
        return 0



        