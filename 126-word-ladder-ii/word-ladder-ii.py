class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:   
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        unorder_map = {}
        unorder_map[beginWord] = 1
        queue =[beginWord]
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        size = len(beginWord)
        result = []
        def dfs(word,seq):
          if word==beginWord:
            result.append(seq[::-1])
            return
          level = unorder_map[word]
          size = len(word)
          for i in range(size):
            for j in range(26):
              char = chr(ord('a')+j)
              newWord = word[:i] + char + word[i+1:]
              if newWord in unorder_map and unorder_map[newWord] + 1 == level:
                seq.append(newWord)
                dfs(newWord,seq)
                seq.pop()

        while queue:
          word = queue.pop(0)
          level = unorder_map[word]
          if word == endWord:
            break
          for i in range(size):
            for j in range(26):
              char = chr(ord('a')+j)
              newWord = word[:i] + char+word[i+1:]
              if newWord in wordSet:
                queue.append(newWord)
                wordSet.remove(newWord)
                unorder_map[newWord] = level+1
        if endWord in unorder_map:
          word = endWord
          seq = [endWord]
          dfs(word,seq)
        return result
       
        