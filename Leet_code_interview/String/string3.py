#First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        uni = []
        used = [False for _ in range(ord('z')-ord('a')+1)]
        a =ord("a")
        for x in s:
            if x in uni: 
                uni.remove(x)
                used[ord(x)-a] = True
            else:
                if not used[ord(x)-a]:
                    uni.append(x)
        if not uni: return -1
        return s.index(uni[0])

