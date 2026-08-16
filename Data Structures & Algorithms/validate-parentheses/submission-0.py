class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        idx = -1

        for i, bracket in enumerate(s):
            if bracket in ['[', '(', '{']:
                stack.append(bracket)
                idx += 1
                # print(idx)
                # print(stack)
            else:
                current = stack.pop()
                current += bracket
                if current not in ['[]', '()', '{}']:
                    return False

        return True