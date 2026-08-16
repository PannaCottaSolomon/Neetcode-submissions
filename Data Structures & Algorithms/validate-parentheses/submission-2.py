class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = []
        idx = -1

        for i, bracket in enumerate(s):
            if bracket in ['[', '(', '{']:
                stack.append(bracket)
                idx += 1
                # print(idx)
                # print(stack)
            elif len(stack) > 0:
                current = stack.pop()
                current += bracket
                if current not in ['[]', '()', '{}']:
                    return False
            else:
                return False

        return True