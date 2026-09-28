class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        ans = left = 0
        has_zero = False # 也可以用+(1-num)的int来代替bool,省去额外的判断
        for right, num in enumerate(nums):
            if num == 0:
                if has_zero:
                    while nums[left] != 0:
                        left += 1
                    left += 1
                else:
                    has_zero = True
            ans = max(ans, right - left)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubarray([1, 1, 0, 1]))
    print(solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
    print(solution.longestSubarray([1, 1, 1]))
