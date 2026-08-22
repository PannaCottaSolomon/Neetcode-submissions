class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for i, char in enumerate(tokens):
            if char not in operations:
                operand = int(char)
                stack.append(operand)
            elif len(stack) == 2:
                operand2 = stack.pop()
                operand1 = stack.pop()
                new = 0
                match char:
                    case "+":
                        new = operand1 + operand2
                    case "-":
                        new = operand1 - operand2
                    case "*":
                        new = operand1 * operand2
                    case "/":
                        new = operand1 // operand2
                stack.append(new) 


        ans = stack.pop()
        return ans