class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        ans = s1 = s2 = 0
        m = n // 2
        for i in range(m, 2 * n - 1):
            s1 += nums[(i - m) % n]
            s2 += nums[i % n]
            left = i - n + 1
            if left < 0:
                continue
            if s1 > s2:
                ans += 1
            s1 -= nums[left]
            s2 -= nums[(left + m) % n]
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countGoodRotations([1, 2, 3, 4, 5, 6]))
    print(solution.countGoodRotations([1, 2, 1, 2]))
