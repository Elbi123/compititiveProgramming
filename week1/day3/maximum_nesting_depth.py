class Solution:
    def maxDepth(self, s):
        """
        :type nums:List[int]
        :rtype: int
        """
        depth = opened = 0
        for char in s:
            if char == "(":
                opened += 1
            if char == ")":
                opened -= 1
            depth = max(depth, opened)
        return depth
