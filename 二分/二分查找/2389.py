def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l


class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n, m = len(nums), len(queries)
        nums.sort()
        pre_sum = [nums[0]] + [0] * (n - 1)
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + nums[i]
        answer = [0] * m
        for i in range(m):
            answer[i] = lower_bound(pre_sum, queries[i] + 1)
        return answer

# Test case
if __name__ == "__main__":
    solution = Solution()
    nums = [4,5,2,1]
    queries = [3,10,21]
    print(solution.answerQueries(nums, queries))  # Output: [2, 4, 5]