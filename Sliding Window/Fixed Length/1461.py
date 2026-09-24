class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 可用字符串滑窗直接统计到集合内,此处用位运算滑窗
        MASK = (1 << k) - 1
        has = [False] * (1 << k)
        cnt = x = 0
        for i, c in enumerate(s):
            # 使用MASK清除掉高于k位的部分(离开滑窗的元素)并在最低位添加新进入滑窗的c
            x = (x << 1 & MASK) | int(c)
            if i - k + 1 < 0 or has[x]:
                continue
            has[x] = True
            # 使用cnt计数,达到2^k即可提前退出
            cnt += 1
            if cnt == 1 << k:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.hasAllCodes("00110110", 2))
    print(solution.hasAllCodes("0110", 1))
    print(solution.hasAllCodes("0110", 2))
