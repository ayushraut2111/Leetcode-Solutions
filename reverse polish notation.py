# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        for i in tokens:
            if i=='+' or i=='-' or i=='*' or i=='/':
                # print(stack)
                a=stack.pop()
                b=stack.pop()
                if i=='+':
                    stack.append(a+b)
                elif i=='-':
                    stack.append(b-a)
                elif i=='*':
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack[0]
    