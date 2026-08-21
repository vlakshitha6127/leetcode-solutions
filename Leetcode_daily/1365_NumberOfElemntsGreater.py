class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li=[]
        for i in nums:
            c=0
            for j in nums:
                if i>j:
                    c+=1
            li.append(c)
        return li

       
