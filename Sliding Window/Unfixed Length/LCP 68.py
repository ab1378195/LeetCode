from typing import List
from collections import Counter


class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        ans = left = 0
        count = Counter()
        for right, flower in enumerate(flowers):
            count[flower] += 1
            while count[flower] > cnt:
                count[flowers[left]] -= 1
                left += 1
            ans += right - left + 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.beautifulBouquet([1, 2, 3, 2], 1))
    print(solution.beautifulBouquet([5, 3, 3, 3], 2))
