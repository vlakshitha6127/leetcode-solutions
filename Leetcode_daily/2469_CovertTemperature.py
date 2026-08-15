class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kel=celsius + 273.15
        far=(celsius * 1.80) + 32.00
        return [kel,far]