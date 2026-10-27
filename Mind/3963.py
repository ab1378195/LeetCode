class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = ["." * n]
        for _ in range(m-1):
            ans.append(("#" * (n - 1) + "."))
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.createGrid(2, 3))
    print(solution.createGrid(3, 3))
    print(solution.createGrid(1, 4))
