class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        li=list(command)
        newli=[]
        for i in range(len(li)):
            if li[i]=="G":
                newli.append(li[i])
            elif li[i]=="(" and li[i+1]==")":
                newli.append("o")
            elif li[i]=="(" and li[i+1]=="a":
                newli.append("al")
            else:
                pass
        return "".join(newli)
