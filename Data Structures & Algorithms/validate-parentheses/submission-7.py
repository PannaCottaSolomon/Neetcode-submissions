class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stk = []
        left = ["(", "{", "["]
        complete = ["()", "{}", "[]"]

        for i, curr in enumerate(s):
            if curr in left:
                stk.append(curr)
            elif len(stk) > 0:
                bracket = stk.pop()
                bracket += curr
                if bracket not in complete:
                    return False
            else:
                return False

        if len(stk) > 0:
            return False

        return True
