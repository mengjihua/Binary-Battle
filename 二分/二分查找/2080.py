from collections import defaultdict

def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l

class RangeFreqQuery(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        pos = defaultdict(list)
        for idx, x in enumerate(arr):
            pos[x].append(idx)
        self.pos = pos   

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        temp = self.pos[value]
        r, l = lower_bound(temp, right + 1), lower_bound(temp, left)
        
        return r - l
                     


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
# 测试
obj = RangeFreqQuery([12,33,4,56,22,2,34,33,22,12,34,56])
print(obj.query(1,2,4))