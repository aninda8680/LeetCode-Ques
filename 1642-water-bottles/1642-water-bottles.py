class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total = 0
        empty= 0
        full = numBottles

        while full > 0:
            total += full
            empty += full
            full = empty // numExchange 
            empty = empty % numExchange

        return total