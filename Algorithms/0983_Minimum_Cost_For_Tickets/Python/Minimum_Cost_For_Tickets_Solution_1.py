
# Space: O(n)
# Time: O(n)

class Solution:
    def mincostTickets(self, days, costs) -> int:
        num_of_days = len(days)
        if num_of_days == 0: return 0
        if num_of_days == 1: return costs[0]

        dp = [0 for _ in range(days[-1] + 1)]
        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                day_pass = dp[i - 1] + costs[0]
                week_pass = dp[max(0, i - 7)] + costs[1]
                month_pass = dp[max(0, i - 30)] + costs[2]
                dp[i] = min(day_pass, week_pass, month_pass)

        return dp[-1]




