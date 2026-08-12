class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ct=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    ct+=1
        return ct
        