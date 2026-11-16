from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        has = {}
        ans = -1
        for num in nums:
            s = 0
            temp = num
            while temp > 0:
                s += temp % 10
                temp //= 10
            if s in has:
                ans = max(ans, num + has[s])
                if num > has[s]:
                    has[s] = num
            else:
                has[s] = num
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumSum([18, 43, 36, 13, 7]))
    print(solution.maximumSum([10, 12, 19, 14]))
