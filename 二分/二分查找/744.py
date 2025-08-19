class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if ord(letters[mid]) >= ord(target) + 1:
                r = mid - 1
            else:
                l = mid + 1
        if l >= len(letters) or letters[l] <= target:
            return letters[0]
        else:
            return letters[l]
        