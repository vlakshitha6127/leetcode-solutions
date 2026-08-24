class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        boxes = 0
        units = 0

        for i in boxTypes:
            
            if boxes + i[0] <= truckSize:
                boxes += i[0]
                units += i[0] * i[1]
            
            else:
                remaining = truckSize - boxes
                units += remaining * i[1]
                break

        return units