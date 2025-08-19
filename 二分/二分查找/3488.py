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

class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        pos = defaultdict(list)
        for idx, x in enumerate(nums):
            pos[x].append(idx)
        # print(pos)

        answer = [-1] * len(queries)
        for i in range(len(queries)):
            idx = queries[i]
            x = nums[idx]
            temp = pos[x]
            
            idx_idx = lower_bound(temp, idx)
            # print(idx, x, temp, idx_idx)
            if len(temp) == 1:
                answer[i] = -1
                continue
            elif len(temp) == 2:
                if idx_idx == 0:
                    answer[i] = min(abs(idx - temp[idx_idx - 1]), idx + 1 + len(nums) - 1 - temp[idx_idx - 1])
                else:
                    answer[i] = min(abs(idx - temp[idx_idx - 1]), len(nums) - 1 - idx + temp[idx_idx - 1] + 1)
                continue
            # l = temp[idx_idx - 1] if idx_idx - 1 >= 0 else len(nums) - 1
            # r = temp[idx_idx + 1] if idx_idx + 1 < len(temp) else 0
            # if l == -1 and r == -1:
            #     answer[i] = -1
            # elif l == -1:
            #     answer[i] = min(r - idx, idx + 1 + len(nums) - 1 - r)
            # elif r == -1:
            #     answer[i] = min(idx - l, len(nums) - 1 - idx + l + 1)
            # else:
            #     answer[i] = min(r - idx, idx - l, len(nums) - 1 - idx + l + 1, idx + 1 + len(nums) - 1 - r)

            if idx_idx == 0:
                answer[i] = min(temp[idx_idx + 1] - idx, idx + 1 + len(nums) - 1 - temp[-1])
            elif idx_idx == len(temp) - 1:
                answer[i] = min(idx - temp[idx_idx - 1], len(nums) - 1 - idx + temp[0] + 1)
            else:
                answer[i] = min(temp[idx_idx + 1] - idx, idx - temp[idx_idx - 1], len(nums) - 1 - idx + temp[0] + 1, idx + 1 + len(nums) - 1 - temp[-1])
        return answer

    def solveQueries2(self, nums, queries):
        indices = defaultdict(list)
        for i, x in enumerate(nums):
            indices[x].append(i)

        n = len(nums)
        for p in indices.values():
            # 前后各加一个哨兵
            i0 = p[0]
            p.insert(0, p[-1] - n)
            p.append(i0 + n)

        for qi, i in enumerate(queries):
            p = indices[nums[i]]
            if len(p) == 3:
                queries[qi] = -1
            else:
                j = lower_bound(p, i)
                queries[qi] = min(i - p[j - 1], p[j + 1] - i)
        return queries

if __name__ == "__main__":
    s = Solution()
    print(s.solveQueries2([1, 3, 1, 4, 1, 3, 2], [0, 3, 5]))