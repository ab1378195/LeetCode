from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        # f[i][y]表示右端点为i,模k后等于y的子数组个数,此处用f记录上个i时的结果
        f = [0] * k
        for v in nums:
            # nf记录本轮i的结果以优化空间
            nf = [0] * k
            nf[v % k] += 1
            for y, c in enumerate(f):
                nf[y * v % k] += c
            f = nf
            for x, c in enumerate(f):
                ans[x] += c
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.resultArray([1, 2, 3, 4, 5], 3))
    print(solution.resultArray([1, 2, 4, 8, 16, 32], 4))
    print(solution.resultArray([1, 1, 2, 1, 1], 2))
