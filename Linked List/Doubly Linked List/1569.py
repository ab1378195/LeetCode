class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)

        # 0 和 n+1 作为哨兵节点
        prev = list(range(-1, n + 1))  # 双向链表的前驱 prev[i] = i - 1
        next = list(range(1, n + 3))   # 双向链表的后继 next[i] = i + 1
        size = [0] * (n + 2)  # 子树大小（节点个数）
        prod = 1  # 分母

        # 自底向上，计算每棵子树的大小
        for x in reversed(nums):
            size[x] = 1

            # x 左右两侧最近的未被删除节点，即为 x 的左右儿子
            left = prev[x]
            if size[left] > 0:
                # 加上左子树的大小
                size[x] += size[left]
                # 删除 left：在 left 的前一个节点与 x 之间建立双向链接
                pl = prev[left]
                prev[x] = pl
                next[pl] = x

            right = next[x]
            if size[right] > 0:
                # 加上右子树的大小
                size[x] += size[right]
                # 删除 right：在 right 的下一个节点与 x 之间建立双向链接
                nr = next[right]
                prev[nr] = x
                next[x] = nr

            prod = prod * size[x] % MOD

        # 计算分子 n!
        fac = 1
        for i in range(2, n + 1):
            fac = fac * i % MOD

        return (fac * pow(prod, -1, MOD) - 1) % MOD