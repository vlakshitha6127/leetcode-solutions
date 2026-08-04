class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ran=max(nums)
        ini=min(nums)
        li=[]
        for i in range (ini,ran):
            if i not in nums:
                li.append(i)
                

        return li
        