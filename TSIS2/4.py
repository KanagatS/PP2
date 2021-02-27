class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        maxht = 0  # start at ground
        maxgain = 0
        for i in gain:
            maxht += i
            maxgain = max(maxht, maxgain)

        return maxgain
