from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        # 统计nums数组中所有数在二进制位的每一位上总共有几个1
        m = max(nums).bit_length()
        cnt = [0] * m
        for num in nums:
            for i in range(m):
                cnt[i] += num >> i & 1
        ans = 0
        for _ in range(k):
            x = 0
            for i in range(m):
                if cnt[i]:
                    cnt[i] -= 1
                    x |= 1 << i
            ans += x * x
        return ans % (10**9 + 7)


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSum([2, 6, 5, 8], 2))
    print(solution.maxSum([4, 5, 4, 7], 3))
