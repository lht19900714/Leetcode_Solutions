class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # calculate minute degree from 0 to current minute
        minutes_degree = 6 * minutes
        # calculate hour degree from 12 to current hour
        hour_degree = (30 * hour + (minutes / 60) * 30) % 360
        res = abs(minutes_degree - hour_degree)
        return res if res <= 180 else 360 - res
