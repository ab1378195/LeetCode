from math import inf


class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        last = -inf
        for i in range(k - 1, -1, -1):
            if nums[i] == key:
                last = i
                break
        ans = []
        n = len(nums)
        for i in range(n):
            if i + k < n and nums[i + k] == key:
                last = i + k  # 这里保证了last<=i+k
            if last >= i - k:  # 因此只检查last>=i-k即可
                ans.append(i)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.findKDistantIndices([3, 4, 9, 1, 3, 9, 5], 9, 1))
    print(solution.findKDistantIndices([2, 2, 2, 2, 2], 2, 2))
