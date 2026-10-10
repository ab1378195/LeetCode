class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        ans = 0
        k = k1 + k2
        for i in range(len(nums1)):
            nums1[i] = abs(nums1[i] - nums2[i])
            ans += nums1[i] * nums1[i]
        if sum(nums1) <= k:
            return 0

        nums = sorted(nums1, reverse=True)
        nums.append(0)
        for i, num in enumerate(nums):
            ans -= num * num
            j = i + 1
            c = j * (num - nums[j])
            if c < k:
                k -= c
                continue
            num -= k // j
            return ans + k % j * (num - 1) * (num - 1) + (j - k % j) * num * num


if __name__ == "__main__":
    solution = Solution()
    print(solution.minSumSquareDiff([1, 2, 3, 4], [2, 10, 20, 19], 0, 0))
    print(solution.minSumSquareDiff([1, 4, 10, 12], [5, 8, 6, 9], 1, 1))
