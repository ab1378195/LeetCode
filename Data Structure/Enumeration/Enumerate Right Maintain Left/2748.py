from typing import List
from math import gcd


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        cnt = [0] * 10
        for num in nums:
            for i, c in enumerate(cnt):
                if gcd(i, num % 10) == 1:
                    ans += c
            while num >= 10:
                num //= 10
            cnt[num] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countBeautifulPairs([2, 5, 1, 4]))
    print(solution.countBeautifulPairs([11, 21, 12]))
