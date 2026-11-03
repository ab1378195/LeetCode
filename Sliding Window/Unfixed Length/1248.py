class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        left1 = left2 = 0
        cnt1 = cnt2 = 0
        ans = 0
        for right, num in enumerate(nums):
            cnt1 += num & 1
            cnt2 += num & 1
            while cnt1 >= k:
                cnt1 -= nums[left1] & 1
                left1 += 1
            while cnt2 > k:
                cnt2 -= nums[left2] & 1
                left2 += 1
            ans += left1 - left2
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfSubarrays([1, 1, 2, 1, 1], 3))
    print(solution.numberOfSubarrays([2, 4, 6], 1))
    print(solution.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
