class Solution:
    def numIdenticalPairs(self, nums):
        """
        :type nums:List[int]
        :rtype: int
        """
        counter = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] == nums[j]:
                    counter += 1
        return counter
