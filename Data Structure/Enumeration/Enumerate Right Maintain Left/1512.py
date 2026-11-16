from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        has = defaultdict(int)
        ans = 0
        for num in nums:
            ans += has[num]
            has[num] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
    print(solution.numIdenticalPairs([1, 1, 1, 1]))
    print(solution.numIdenticalPairs([1, 2, 3]))
