class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        li=[]
        for i in order:
            if i in friends:
                li.append(i)
        return li

        