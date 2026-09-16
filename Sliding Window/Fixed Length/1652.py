from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        r = k + 1 if k > 0 else n
        k = abs(k)
        s = sum(code[r - k : r])
        ans = [0] * n
        for i in range(n):
            ans[i] = s
            s += code[r % n] - code[(r - k) % n]
            r += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.decrypt([5, 7, 1, 4], 3))
    print(solution.decrypt([1, 2, 3, 4], 0))
    print(solution.decrypt([2, 4, 9, 3], -2))
