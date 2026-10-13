from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # 排序键可以直接用平方而非绝对值,这样后续也不用再算平方了
        nums.sort(key=abs, reverse=True)
        n = (len(nums) + 1) // 2
        ans = 0
        for num in nums[:n]:
            ans += num * num
        for num in nums[n:]:
            ans -= num * num
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxAlternatingSum([1, 2, 3]))
    print(solution.maxAlternatingSum([1, -1, 2, -2, 3, -3]))
