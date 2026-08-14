class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odds=0
        eves=0
        for i in range(len(nums)):
            if i%2==0:
                eves+=nums[i]
            else:
                odds+=nums[i]
        return eves-odds