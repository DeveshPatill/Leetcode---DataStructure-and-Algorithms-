class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        # Create an empty list of the same length
        result = [""] * len(s)
        
        # Place each character at its target position
        for i, ch in enumerate(s):
            result[indices[i]] = ch
        
        # Join list into string
        return "".join(result)