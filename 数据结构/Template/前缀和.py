class PrefixSum:
    def __init__(self, nums: list, is2D: bool = False):
        if is2D:
            self.preSum = self.getPrefixSum2D(nums)
        else:
            self.preSum = self.getPrefixSum1D(nums)

    def getPrefixSum2D(self, nums: list) -> list:
        m, n = len(nums), len(nums[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + nums[i - 1][j - 1]
        return pre
    
    def getPrefixSum1D(self, nums: list) -> list:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]
        return pre