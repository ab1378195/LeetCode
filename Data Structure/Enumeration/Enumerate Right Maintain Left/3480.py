from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        groups = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            if a > b:
                groups[b].append(a)
            else:
                groups[a].append(b)

        ans = 0
        extra = [0] * (n + 2)
        # b负责维护左端点为i时,会使得右端点不合法的最小的两个右端点值
        b = [n + 1, n + 1]
        for i in range(n, 0, -1):
            if groups[i]:
                b += groups[i]
                b.sort()
                b = b[:2]
            ans += b[0] - i
            extra[b[0]] += b[1] - b[0]
        return ans + max(extra)


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubarrays(4, [[2, 3], [1, 4]]))
    print(solution.maxSubarrays(5, [[1, 2], [2, 5], [3, 5]]))
