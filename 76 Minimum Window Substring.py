class Solution:
    def minWindow(self, s: str, t: str) -> str:
        begin, end = -1, -1
        i, j = 0, -1
        n = len(s)
        sum = 0
        tMap = {}
        sMap = {}
        for l in t:
            if l not in tMap:
                tMap[l] = 0
            tMap[l] += 1
            sum += 1

        while i < n:
            if sum > 0:
                j += 1
                if j == n:
                    if begin != -1:
                        return s[begin : end + 1]
                    return ""
                if s[j] in tMap:
                    if s[j] not in sMap:
                        sMap[s[j]] = 0
                    sMap[s[j]] += 1
                    if sMap[s[j]] <= tMap[s[j]]:
                        sum -= 1
            else:
                if begin == -1 or j - i + 1 < end - begin + 1:
                    begin, end = i, j
                if s[i] in tMap:
                    sMap[s[i]] -= 1
                    if sMap[s[i]] < tMap[s[i]]:
                        sum += 1
                i += 1
                if i == n:
                    if begin != -1:
                        return s[begin : end + 1]
                    return ""
                