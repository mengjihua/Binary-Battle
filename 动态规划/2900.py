from typing import List
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, permutations

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        words.sort()
        