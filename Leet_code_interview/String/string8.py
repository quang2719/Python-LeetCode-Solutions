class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for x in strs:
                if len(x) <= i or x[i]!=strs[0][i]:
                    return res
            res += strs[0][i]
        return res