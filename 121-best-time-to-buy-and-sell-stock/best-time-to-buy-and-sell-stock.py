class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Buy day
        right = 1  # Sell day
        max_profit = 0

        while right < len(prices):
        # If current price is greater than buy price → possible profit
             if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
             else:
            # Move buy day to current day (lower price found)
               left = right
             right += 1

        return max_profit