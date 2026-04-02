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
            else:
                if len(stack) == 0:
                    return False
                
                current = stack.pop()
                current += bracket
                if current not in ['[]', '()', '{}']:
                    return False
                
        if len(stack) != 0:
            return False        
        return True