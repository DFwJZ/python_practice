#Leetcode 496
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []

        for num in nums1:
            found = False
            greater = -1
            for n in nums2:
                if n == num:
                    found = True
                elif found and n > num:
                    greater = n
                    break
            res.append(greater)

        return res
    
    def nextGreaterElementHashMap(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        nxt_greater = {}

        for x in nums2:
            while stack and stack[-1] < x:
                nxt_greater[stack.pop()] = x
            stack.append(x)

        res = []
        for num in nums1:
            res.append(nxt_greater.get(num, -1))
        return res


def main():
    solution = Solution()
    nums1 = [2,4]
    nums2 = [1,2,3,4,2,4,6]

    print(solution.nextGreaterElement(nums1, nums2))
    print(solution.nextGreaterElementHashMap(nums1, nums2))

if __name__ == '__main__':
    main()   
