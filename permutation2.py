# Leetcode 47

# Problem Statement
"""
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

"""
import logging.config
from typing import List
import logging

# logging.basicConfig(level=logging.INFO)

class Solution:
    def __init__(self):
        self.logger = logging.getLogger(f"{self.__class__.__name__}")
        self.logger.setLevel(logging.WARNING)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # logger_name = f"{self.__class__.__name__}.{self.permuteUnique.__name__}"

        res = []
        perm = []
        count = { n:0 for n in nums}

        for n in nums:
            count[n] +=1
        
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop()

        dfs()
        return res

    def permuteUnique1(self, nums: List[int]) -> List[List[int]]: 
        res = []
        perm = []
        freq = {n:0 for n in nums}

        for i in nums:
            freq[i] += 1

        print(freq)

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in freq:
                if freq[n] > 0:
                    perm.append(n)
                    freq[n] -= 1
                    
                    dfs()

                    freq[n] += 1
                    perm.pop()
        
        dfs()
        return res
            


def main():
    solution = Solution()
    test = [1,1,2]
    res = solution.permuteUnique1(test)

    print(res)



if __name__ == '__main__':
    main()