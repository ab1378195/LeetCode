from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)

        def check(a: List[List[int]]) -> bool:
            """检查能否水平分割"""
            m, n = len(a), len(a[0])

            def f(a: List[List[int]]) -> bool:
                """删除掉上半部分一个数字,判断是否满足要求"""
                st = {0}  # 0对应不删除数字
                s = 0
                for i, row in enumerate(a[:-1]):
                    for j, num in enumerate(row):
                        s += num
                        if i > 0 or j == 0 or j == n - 1:
                            st.add(num)
                    # 特殊处理仅1行的情况
                    if n == 1:
                        if (
                            s * 2 == total
                            or s * 2 - total == a[0][0]
                            or s * 2 - total == row[0]
                        ):
                            return True
                        continue
                    if s * 2 - total in st:
                        return True
                    # 当执行到后续行时第一行的元素也可被选择为删除的元素,添加到集合中
                    if i == 0:
                        st.update(row)
                return False

            # 两种情况:删掉上半部分的数字和删掉下半部分的数字
            return f(a) or f(a[::-1])
        # 两种情况:水平分割和竖直分割
        return check(grid) or check(list(zip(*grid)))
