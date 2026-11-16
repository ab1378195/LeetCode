from typing import List
from collections import defaultdict


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        cnt = defaultdict(int)
        ans = []
        for num in nums:
            if cnt[target - num]:
                ans.append([target - num, num])
                cnt[target - num] -= 1
            else:
                cnt[num] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.pairSums([5, 6, 5], 11))
    print(solution.pairSums([5, 6, 5, 6], 11))
