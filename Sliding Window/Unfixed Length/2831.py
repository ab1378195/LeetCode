from typing import List
from collections import defaultdict


class Solution:
    """以元素值为键,记录每个元素在数组中的索引,则对于num的等值子数组,其包含的元素索引为pos_lists[num].
    记该数组为pos,窗口左右端点为left和right,则要获得num的等值子数组,需要删去[pos[left],post[right]]中不为num的数.
    由于该区间内为num的数有right-left+1,所以要删去的数是pos[right]-pos[left]+right-left.
    注意到pos存储pos[i]-i可化简上式,即每个pos内的数都减去其在pos内的索引,从而删去的数变为pos[right]-pos[left]
    """

    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos_lists = defaultdict(list)
        for i, num in enumerate(nums):
            pos_lists[num].append(i - len(pos_lists[num]))
        ans = 0
        for pos in pos_lists.values():
            if len(pos) <= ans:
                continue
            left = 0
            for right, p in enumerate(pos):
                while p - pos[left] > k:
                    left += 1
                ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestEqualSubarray([1, 3, 2, 3, 1, 3], 3))
    print(solution.longestEqualSubarray([1, 1, 2, 2, 1, 1], 2))
