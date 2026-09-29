class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        order: list[int] = []
        top: int = 0
        bottom: int = len(matrix) - 1
        left: int = 0
        right: int = len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                order.append(matrix[top][col])
            top += 1
            for row in range(top, bottom + 1):
                order.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    order.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    order.append(matrix[row][left])
                left += 1

        return order
def print_values(values: list[int]) -> None:
    print(values)
def main() -> None:
    matrix: list[list[int]] = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    sol: Solution = Solution()

    result: list[int] = sol.spiralOrder(matrix)
    print_values(result)
if __name__ == "__main__":
    main()