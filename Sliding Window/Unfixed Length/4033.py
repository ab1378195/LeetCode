from collections import defaultdict
from random import randrange


class Solution:
    """出现次数频率为偶数等价于异或和为0,计算任意子数组的异或和可用前缀和.
    虽然本题每个查询不一样,但是要求的恰好包含k个不同数字中k是不变的,因此可以基于k构造滑动窗口.
    """

    def validSubarrays(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[bool]:
        n = len(nums)
        s = [0] * (n + 1)
        # 异或哈希
        mp = defaultdict(lambda: randrange(10**10))
        for i, num in enumerate(nums):
            s[i + 1] = s[i] ^ mp[num]

        def calc_left(k: int) -> list[int]:
            lefts = [0] * n
            cnt = defaultdict(int)
            left = 0
            for i, num in enumerate(nums):
                cnt[num] += 1
                while len(cnt) >= k:
                    out = nums[left]
                    if cnt[out] == 1:
                        del cnt[out]
                    else:
                        cnt[out] -= 1
                    left += 1
                lefts[i] = left
            return lefts

        l1 = calc_left(k + 1)
        l2 = calc_left(k)
        return [s[r + 1] == s[l] and l1[r] <= l < l2[r] for l, r in queries]


if __name__ == "__main__":
    solution = Solution()
    print(solution.validSubarrays([1, 2, 2, 1], 2, [[0, 1], [0, 3], [1, 2]]))
    print(solution.validSubarrays([3, 3, 3], 1, [[1, 2], [0, 2]]))
