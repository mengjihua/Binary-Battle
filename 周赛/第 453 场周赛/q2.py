from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        complexity = [(i, idx) for i, idx in enumerate(complexity)]
        complexity.sort(key=lambda x: x[0])