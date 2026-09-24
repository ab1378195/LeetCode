from typing import List


class Solution:
    """找第x小的数就是找到最小的v满足<=v的数至少有x个,本题中num的范围较小,因此可用计数排序的思路维护窗口内各个数的出现次数"""

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = [0] * 101
        for num in nums[: k - 1]:
            cnt[num] += 1
        ans = [0] * (len(nums) - k + 1)
        for i, (in_, out) in enumerate(zip(nums[k - 1 :], nums)):
            cnt[in_] += 1
            left = x
            for v in range(-50, 0):
                left -= cnt[v]
                if left <= 0:
                    ans[i] = v
                    break
            cnt[out] -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.getSubarrayBeauty([1, -1, -3, -2, 3], 3, 2))
    print(solution.getSubarrayBeauty([-1, -2, -3, -4, -5], 2, 2))
    print(solution.getSubarrayBeauty([-3, 1, 2, -3, 0, -3], 2, 1))
