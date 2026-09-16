from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = sum(nums)
        if k <= 1:
            return 0
        ans = 0
        cnt = sum(nums[-k + 1 :])
        for i, num in enumerate(nums):
            cnt += num
            ans = max(ans, cnt)
            cnt -= nums[i - k + 1]
        return k - ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minSwaps([0, 1, 0, 1, 1, 0, 0]))
    print(solution.minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]))
    print(solution.minSwaps([1, 1, 0, 0, 1]))
    print(solution.minSwaps([1]))
