class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(target, cur):
            if target < 0 or cur >= len(candidates):
                return
            if target == 0:
                res.append(comb.copy())
                return
            
            comb.append(candidates[cur])
            dfs(target-candidates[cur], cur)
            comb.pop()
            dfs(target, cur+1)
        
        dfs(target, 0)
        return res
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
                backtrack(i, target-candidates[i], path, result)
                path.pop()

        candidates.sort()
        result = []
        backtrack(0, target, [], result)
        return result


        