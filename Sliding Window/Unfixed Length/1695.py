class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        ans = left = score = 0
        cnt = set()
        for right, num in enumerate(nums):
            score += num
            while num in cnt:
                cnt.remove(nums[left])
                score -= nums[left]
                left += 1
            cnt.add(num)
            ans = max(ans, score)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumUniqueSubarray([4, 2, 4, 5, 6]))
    print(solution.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))
