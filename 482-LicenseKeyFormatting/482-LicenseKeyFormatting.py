# Last updated: 7/14/2026, 9:56:13 AM
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace("-","").upper()
        ans=""
        while len(s)>k:
            ans="-"+s[-k:]+ans
            s=s[:-k]
        return s+ans