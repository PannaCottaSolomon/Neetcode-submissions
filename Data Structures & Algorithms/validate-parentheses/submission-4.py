class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        left = ["(", "{", "["]
        complete = ["()", "{}", "[]"]

        for i, curr in enumerate(s):
            if curr in left:
                stk.append(curr)
            else:
                bracket = stk.pop()
                bracket += curr
                if bracket not in complete:
                    return False

        return True
