from math import isqrt


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        next_desc = [0] * n
        next_desc[-1] = p = n
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                p = i
            next_desc[i] = p

        def solve(k: int) -> None:
            last_max = 0
            for r in range(k - 1, n, k):
                l = r - k + 1
                m = next_desc[l]
                if m >= r:
                    if nums[l] < last_max:
                        return
                    last_max = nums[r]
                else:
                    if (
                        next_desc[m + 1] < r
                        or nums[m + 1] < last_max
                        or nums[r] > nums[l]
                    ):
                        return
                    last_max = nums[m]
            nonlocal ans
            ans += k

        ans = 0
        for k in range(1, isqrt(n) + 1):
            if n % k == 0:
                solve(k)
                if k * k < n:
                    solve(n // k)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.sortableIntegers([3, 1, 2]))
    print(solution.sortableIntegers([7, 6, 5]))
    print(solution.sortableIntegers([5, 8]))
