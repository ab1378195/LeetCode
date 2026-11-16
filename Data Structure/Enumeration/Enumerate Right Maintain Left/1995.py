from typing import List
from collections import defaultdict


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        cnt3 = defaultdict(int)
        ans = 0
        for num in nums:
            ans += cnt3[num]
            for value in cnt2.keys():
                cnt3[value + num] += cnt2[value]
            for value in cnt1.keys():
                cnt2[value + num] += cnt1[value]
            cnt1[num] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countQuadruplets([1, 2, 3, 6]))
    print(solution.countQuadruplets([3, 3, 6, 4, 5]))
    print(solution.countQuadruplets([1, 1, 1, 3, 5]))
