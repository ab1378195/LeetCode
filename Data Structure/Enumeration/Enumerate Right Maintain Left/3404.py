from typing import List
from collections import defaultdict


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        # 4个数按索引顺序记为a,b,c,d
        ans = 0
        cnt = defaultdict(int)
        # i为c的位置
        for i in range(4, len(nums) - 2):
            b = nums[i - 2]
            # 枚举a
            for a in nums[: i - 3]:
                cnt[a / b] += 1

            c = nums[i]
            # 枚举d
            for d in nums[i + 2 :]:
                ans += cnt[d / c]
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfSubsequences([1, 2, 3, 4, 3, 6, 1]))
    print(solution.numberOfSubsequences([3, 4, 3, 4, 3, 4, 3, 4]))
