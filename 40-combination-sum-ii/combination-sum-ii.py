class Solution:
    def findCombination(self, index, target, candidates, result, each_result):
        if target == 0:
            result.append(each_result.copy())
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i]== candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            each_result.append(candidates[i])
            self.findCombination(i+1, target-candidates[i], candidates, result, each_result)
            each_result.pop()
   
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        each_result = []
        candidates.sort()
        self.findCombination(0, target, candidates, result, each_result)
        return result
        def backtrack(start, target, path, result):
            if target== 0:
                result.append(path[:])
                return 
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i> start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, target-candidates[i], path, result)
                path.pop()

        candidates.sort()
        result = []
        backtrack(0, target, [], result)
        return result
    