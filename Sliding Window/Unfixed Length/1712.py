from itertools import accumulate
from bisect import bisect_left, bisect_right


class Solution:
    def waysToSplit(self, nums: list[int]) -> int:
        s = list(accumulate(nums, initial=0))
        n = len(nums)
        ans = 0
        for right in range(2, n):
            if 3 * s[right] > 2 * s[n]:
                break
            i = bisect_left(s, 2 * s[right] - s[n], 1, right)
            j = bisect_right(s, s[right] // 2, i, right)
            ans += j - i
        return ans % (10**9 + 7)


if __name__ == "__main__":
    solution = Solution()
    print(solution.waysToSplit([1, 1, 1]))
    print(solution.waysToSplit([1, 2, 2, 2, 5, 0]))
    print(solution.waysToSplit([3, 2, 1]))
