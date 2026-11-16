class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        has = {}
        max_prod = -10001
        ans = [-1, -1]
        for i, num in enumerate(nums):
            if target - num != num and target - num in has:
                if num * (target - num) > max_prod:
                    ans = [i, has[target - num]]
                    max_prod = num * (target - num)
            else:
                has[num] = i
        if nums[ans[0]] > nums[ans[1]]:
            return ans
        return [ans[1], ans[0]]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProductPair([1, 2, 3, 4], 5))
    print(solution.maxProductPair([-3, -1, 4, 2], 1))
    print(solution.maxProductPair([3, 3, 5], 6))
