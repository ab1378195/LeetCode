from typing import List
from random import randint
from collections import defaultdict


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 1_070_777_777
        BASE = randint(8 * 10**8, 9 * 10**8)
        pow_base = [1] + [0] * n
        pre_hash = [0] * (n + 1)
        for i, num in enumerate(nums):
            pow_base[i + 1] = pow_base[i] * BASE % MOD
            pre_hash[i + 1] = (pre_hash[i] * BASE + num) % MOD

        def sub_hash(l: int, r: int) -> int:
            return (pre_hash[r] - pre_hash[l] * pow_base[r - l]) % MOD

        def check(length: int) -> bool:
            cnt = defaultdict(int)
            for i in range(length, n + 1):
                h = sub_hash(i - length, i)
                cnt[h] += 1
            return 1 in cnt.values()

        # 二分查找符合要求的子串长度
        left, right = 0, n
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right


if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestUniqueSubarray([3, 3, 3]))
    print(solution.smallestUniqueSubarray([2, 1, 2, 3, 3]))
    print(solution.smallestUniqueSubarray([1, 1, 2, 2, 1]))
