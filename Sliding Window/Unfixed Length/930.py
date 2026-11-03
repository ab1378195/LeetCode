class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        ans = 0
        left1 = left2 = 0
        s1 = s2 = 0
        for right, num in enumerate(nums):
            s1 += num
            while left1 <= right and s1 >= goal:
                s1 -= nums[left1]
                left1 += 1
            ans += left1
            s2 += num
            while left2 <= right and s2 > goal:
                s2 -= nums[left2]
                left2 += 1
            ans -= left2
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
    print(solution.numSubarraysWithSum([0, 0, 0, 0, 0], 0))
