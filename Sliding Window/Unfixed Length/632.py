from math import inf


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        pairs = sorted((num, i) for (i, arr) in enumerate(nums) for num in arr)
        ans_l, ans_r = -inf, inf
        less = len(nums)
        cnt = [0] * less
        left = 0
        for num, i in pairs:
            if cnt[i] == 0:
                less -= 1
            cnt[i] += 1
            while less == 0:
                out_num, out_source = pairs[left]
                if num - out_num < ans_r - ans_l:
                    ans_l, ans_r = out_num, num
                if cnt[out_source] == 1:
                    less += 1
                cnt[out_source] -= 1
                left += 1
        return [ans_l, ans_r]


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
    )
    print(solution.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
