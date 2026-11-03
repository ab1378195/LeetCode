from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        less1 = less2 = left1 = left2 = ans = 0
        for right, num in enumerate(nums):
            cnt1[num] += 1
            if cnt1[num] == m:
                less1 += 1
            cnt2[num] += 1
            if cnt2[num] == m:
                less2 += 1
            while less1 >= k:
                if cnt1[nums[left1]] == m:
                    less1 -= 1
                cnt1[nums[left1]] -= 1
                left1 += 1
            while less2 > k:
                if cnt2[nums[left2]] == m:
                    less2 -= 1
                cnt2[nums[left2]] -= 1
                left2 += 1
            ans += left1 - left2
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubarrays([1, 2, 1, 2, 2], 2, 2))
    print(solution.countSubarrays([3, 1, 2, 4], 2, 1))
    print(solution.countSubarrays([1, 1, 9966], 1, 2))
