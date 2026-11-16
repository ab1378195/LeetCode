from typing import List
from collections import Counter


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        cnt = Counter(x + y for x in nums1 for y in nums2)
        return sum(cnt[-x - y] for x in nums3 for y in nums4)


if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
    print(solution.fourSumCount([0], [0], [0], [0]))
