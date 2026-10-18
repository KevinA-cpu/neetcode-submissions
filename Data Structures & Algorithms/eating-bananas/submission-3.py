class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = min(sum(piles) // h, 1)
        r = max(piles)

        def getHours(r):
            if r == 0:
                return float('Inf')

            hours = 0
            for i in piles:
                hours += math.ceil(i/r)
            return hours

        minRates = r
        while(l <= r):
            mid = l + (r-l) // 2
            hours = getHours(mid)
            if hours > h:
                l = mid + 1
            elif hours <= h:
                if minRates == -1 or minRates > mid:
                    minRates = mid
                r = mid - 1
        return minRates
