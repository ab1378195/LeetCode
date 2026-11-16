class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = 10001
        ans = 0
        for price in prices:
            ans = max(ans, price - min_price)
            min_price = min(min_price, price)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit([7, 6, 4, 3, 1]))
