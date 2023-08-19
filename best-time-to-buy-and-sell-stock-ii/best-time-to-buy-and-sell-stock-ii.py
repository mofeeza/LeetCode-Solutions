class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximumProfit = 0

        for i in range(1, len(prices)):
            # Calculate the difference between the current and previous day's prices
            currentMaximumProfit = prices[i] - prices[i - 1]
            # If the difference is positive, add it to the maximum profit
            if currentMaximumProfit > 0:
                maximumProfit += currentMaximumProfit

        return maximumProfit