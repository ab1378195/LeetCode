class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num * 9 < sum:
            return ""
        ans = "9" * (sum // 9)
        if sum % 9:
            ans += str(sum % 9)
        return ans + "0" * (num - len(ans))


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSumOfSquares(2, 3))
    print(solution.maxSumOfSquares(2, 17))
    print(solution.maxSumOfSquares(1, 10))
