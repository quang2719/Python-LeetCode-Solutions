#Valid Anagram


def isAnagram( s, t):
    a = ord('a')
    d1 = [0 for _ in range((ord('z')-ord("a"))+1)]
    d2 = d1.copy()
    for x in s:
        d1[(ord(x)-a)] += 1
    for x in t:
        d2[ord(x)-a] += 1
    return d1==d2
print(isAnagram("art", "tr"))