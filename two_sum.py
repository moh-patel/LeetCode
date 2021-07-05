class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        size = len(nums)
        for i in range(size-1):
            for j in range(1,size):
                if i!=j and nums[i]+nums[j] == target:
                    return [i,j]


# solution on https://www.youtube.com/watch?v=KLlXCFG5TnA, takes less time but uses more memory
# time O(n)
# space O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i,n in enumerate(nums):
            diff = target -n 
            if diff in prevMap:
                return {prevMap[diff], i}
            prevMap[n] = i