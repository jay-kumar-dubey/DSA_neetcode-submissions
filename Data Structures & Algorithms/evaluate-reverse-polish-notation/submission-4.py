class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens:
            if i not in ['+','-','/','*']:
                stack.append(int(i))
            
            elif i == '+' :
                val = stack.pop() + stack.pop()
                stack.append(val)
            
            elif i == '-':
                val = - stack.pop() + stack.pop()
                stack.append(val)

            elif i == '*':
                val = stack.pop() * stack.pop()
                stack.append(val)

            else:
                v = stack.pop()
                val = int(stack.pop() / v)
                stack.append(val)

        return stack.pop()
