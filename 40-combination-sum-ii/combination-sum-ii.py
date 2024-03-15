class Solution:
   
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
    