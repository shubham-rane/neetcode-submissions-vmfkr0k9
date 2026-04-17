class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        ans = 0
        while left < right and right < len(prices):
            # print(left, right)
            if prices[left] < prices [right]:
                profit = prices[right] - prices[left]
                if ans < profit:
                    ans = profit
                right += 1
            else:
                left = right
                right += 1
        return ans


        