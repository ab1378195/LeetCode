from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for dominoe in dominoes:
            temp = tuple(sorted(dominoe))
            ans += cnt[temp]
            cnt[temp] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
    print(solution.numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))
