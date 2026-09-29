from collections import defaultdict


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right, answer in enumerate(answerKey):
            cnt[answer] += 1
            while cnt["T"] > k and cnt["F"] > k:
                cnt[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxConsecutiveAnswers("TTFF", 2))
    print(solution.maxConsecutiveAnswers("TFFT", 1))
    print(solution.maxConsecutiveAnswers("TTFTTFTT", 1))
