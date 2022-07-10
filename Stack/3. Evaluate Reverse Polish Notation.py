class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for t in tokens:
            if t not in operators:
                stack += [t]
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if t == '+':
                    exp = a + b
                elif t == '-':
                    exp = a - b
                elif t == '*':
                    exp = a * b
                else:
                    exp = int(a / b)
                stack.append(exp)
                
        print(stack)
        return stack[0]
