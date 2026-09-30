from collections import defaultdict

MX = 100_001
prime_factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not prime_factors[i]:
        for j in range(i, MX, i):
            prime_factors[j].append(i)


class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        left = ans = 0
        cnt = defaultdict(int)
        for right, num in enumerate(nums):
            for prime_factor in prime_factors[num]:
                cnt[prime_factor] += 1
            while len(cnt) > k:
                for prime_factor in prime_factors[nums[left]]:
                    cnt[prime_factor] -= 1
                    if cnt[prime_factor] == 0:
                        del cnt[prime_factor]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubarray([7, 6, 10, 12, 11], 3))
    print(solution.longestSubarray([4, 6, 9, 18], 4))
    print(solution.longestSubarray([6, 10, 15], 2))
