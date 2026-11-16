from typing import List


class Solution:
    """该类线段覆盖题目注意是在滑动数组的下标,而非数组内的具体距离"""

    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        if k * 2 + 1 >= prizePositions[-1] - prizePositions[0]:
            return n
        # mx[i+1]:右端点<=prizePositions[i]的线段可覆盖礼物的最大数量
        mx = [0] * (n + 1)
        # 设右侧线段的右端点在prizePositions[right]时,最左侧能被覆盖的礼物的位置为prizePositions[left]
        ans = left = 0
        for right, position in enumerate(prizePositions):
            # 找到右侧线段当前右端点对应的left
            while position - prizePositions[left] > k:
                left += 1
            # 此时右侧线段能覆盖的礼物数量即为right-left+1(这就是滑窗要滑动数组下标的原因,方便统计覆盖的礼物数目)
            ans = max(ans, mx[left] + right - left + 1)
            # 由于两条线段一样长,所以当左侧线段的右端点到了right时,能覆盖的最大礼物数量和右侧线段右端点在right时的覆盖数量一样
            # 然后取右端点放在right和不放在right,即为mx[right+1]
            mx[right + 1] = max(mx[right], right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximizeWin([1, 1, 2, 2, 3, 3, 5], 2))
    print(solution.maximizeWin([1, 2, 3, 4], 0))
