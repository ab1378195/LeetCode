from math import atan2, degrees


class Solution:
    def visiblePoints(
        self, points: list[list[int]], angle: int, location: list[int]
    ) -> int:
        angles = []
        same = 0
        for point in points:
            dy = point[1] - location[1]
            dx = point[0] - location[0]
            if dx == 0 and dy == 0:
                same += 1
                continue
            angles.append(degrees(atan2(dy, dx)))
        angles.sort()
        angles += [a + 360 for a in angles if a < angle]
        ans = left = 0
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            ans = max(ans, right - left + 1)
        return ans + same


if __name__ == "__main__":
    solution = Solution()
    print(solution.visiblePoints([[2, 1], [2, 2], [3, 3]], 90, [1, 1]))
    print(solution.visiblePoints([[2, 1], [2, 2], [3, 4], [1, 1]], 90, [1, 1]))
    print(solution.visiblePoints([[1, 0], [2, 1]], 13, [1, 1]))
    print(solution.visiblePoints([[0, 0], [0, 2]], 90, [1, 1]))
