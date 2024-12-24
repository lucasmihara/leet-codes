class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        start, end = 0, n-1
        mid = 0
        lastLess = 0
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] == target:
                lastLess = mid
                break
            elif matrix[mid][0] > target:
                end = mid - 1
            elif matrix[mid][0] <= target:
                lastLess = mid
                start = mid + 1
        i = lastLess
        n = len(matrix[0])
        start, end = 0, n-1
        mid = 0
        while start <= end:
            mid = (start + end) // 2
            if matrix[i][mid] == target:
                return True
            if matrix[i][mid] > target:
                end = mid - 1
            elif matrix[i][mid] <= target:
                start = mid + 1
        return matrix[i][mid] == target