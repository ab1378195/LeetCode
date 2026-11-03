class Solution:
    def maximizeWin(self, prizePositions: list[int], k: int) -> int:
        n = len(prizePositions)
        if 2 * k + 1 >= prizePositions[-1] - prizePositions[0]:
            return n
        ans = mx = left = right = 0
        for mid, position in enumerate(prizePositions):
            # 先更新右侧线段,right是第一个导致线段过长的数组下标,即right-1是线段最远能覆盖到的礼物对应的数组下标
            while right < n and prizePositions[right] - position <= k:
                right += 1
            # prizePositions[mid]是右侧线段的左端点
            # 此时左侧线段的右端点小于等于prizePositions[mid-1](贪心:线段不重叠)
            # mx是所有这样的左侧线段能覆盖礼物的最大值
            ans = max(ans, mx + right - mid)
            # 此时mid是左侧线段的右端点,要把mx更新为右端点小于等于prizePositions[mid]的线段覆盖礼物的最大值
            while position - prizePositions[left] > k:
                left += 1
            mx = max(mx, mid - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximizeWin([1, 1, 2, 2, 3, 3, 5], 2))
    print(solution.maximizeWin([1, 2, 3, 4], 0))
