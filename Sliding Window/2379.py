class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = k
        count = 0
        for i, block in enumerate(blocks):
            if block == "W":
                count += 1
            if i < k - 1:
                continue
            ans = min(ans, count)
            if blocks[i - k + 1] == "W":
                count -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumRecolors("WBBWWBBWBW", 7))
    print(solution.minimumRecolors("WBWBBBW", 2))
