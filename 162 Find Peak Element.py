class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n-1
        mid = 0
        while start <= end:
            mid = (start + end)//2
            right = True if mid >= n-1 else nums[mid] > nums[mid+1]
            left = True if mid <= 0 else nums[mid] > nums[mid-1]
            if left and right:
                return mid
            if not right:
                start = mid + 1
            elif not left:
                end = mid - 1
        return mid