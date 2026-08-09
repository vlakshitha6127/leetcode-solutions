class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ct=0
        for i in nums:
            if i<0:
                ct+=1
            elif i==0:
                return 0
        if ct%2==0:
            return 1
        else:
            return -1
    