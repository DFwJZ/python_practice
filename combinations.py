#Leetcode 77


from typing import List
# import copy

class Solution:
    def combinations(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, combination):
            if len(combination) == k:
                res.append(combination.copy())
                return
            
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()

        
        backtrack(1, [])

        return res
    

def main():
    solution = Solution()
    n = 4
    k = 2
    res = solution.combinations1(n,k)

    print(res)



if __name__ == '__main__':
    main()   