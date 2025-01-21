class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        self.maxes = {
            True: [0] * n,
            False: [0] * n
        }
        return max(self.solve(nums, 0, False), self.solve(nums, 0, True))
    def solve(self, nums, pos, lastVis):
        n = len(nums)
        if pos >= n:
            return 0
        if self.maxes[lastVis][pos] > 0:
            return self.maxes[lastVis][pos]
        if not lastVis and nums[pos] != 0:
            r = self.solve(nums, pos + 1, True) + nums[pos]
            if r > self.maxes[lastVis][pos]:
                self.maxes[lastVis][pos] = r
        r = self.solve(nums, pos + 1, False)
        if r > self.maxes[lastVis][pos]:
            self.maxes[lastVis][pos] = r
        return self.maxes[lastVis][pos]