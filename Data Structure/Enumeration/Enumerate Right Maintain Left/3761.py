from typing import List
from math import inf


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        has = {}
        ans = inf
        for i, num in enumerate(nums):
            if num in has:
                ans = min(ans, i - has[num])
            has[int(str(num)[::-1])] = i
        return -1 if ans == inf else ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minMirrorPairDistance([12, 21, 45, 33, 54]))
    print(solution.minMirrorPairDistance([120, 21]))
    print(solution.minMirrorPairDistance([21,120]))
