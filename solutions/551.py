class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") <2 and s.count("LLL") <1:
            return True
        return False