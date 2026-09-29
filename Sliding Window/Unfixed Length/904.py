from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right, fruit in enumerate(fruits):
            cnt[fruit] += 1
            while len(cnt) > 2:
                out = fruits[left]
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.totalFruit([1, 2, 1]))
    print(solution.totalFruit([0, 1, 2, 2]))
    print(solution.totalFruit([1, 2, 3, 2, 2]))
