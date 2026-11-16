from math import inf


class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # suf_min[i]为左端点>=i的和为target的子数组的最短长度
        suf_min = [0] * n
        min_len = inf
        s = 0
        right = n - 1
        # 用滑窗初始化suf_min
        for left in range(n - 1, 0, -1):
            s += arr[left]
            while s > target:
                s -= arr[right]
                right -= 1
            if s == target:
                min_len = min(min_len, right - left + 1)
            suf_min[left] = min_len

        ans = inf
        s = left = 0
        for right in range(n - 1):
            s += arr[right]
            while s > target:
                s -= arr[left]
                left += 1
            if s == target:
                ans = min(ans, right - left + 1 + suf_min[right + 1])
        return -1 if ans == inf else ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minSumOfLengths([3, 2, 2, 4, 3], 3))
    print(solution.minSumOfLengths([7, 3, 4, 7], 7))
    print(solution.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6))
    print(solution.minSumOfLengths([5, 5, 4, 4, 5], 3))
    print(solution.minSumOfLengths([3, 1, 1, 1, 5, 1, 2, 1], 3))
