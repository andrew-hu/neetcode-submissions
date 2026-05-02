class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        # iterate through array (while loop)
        while i < len(s):

            if len(stack) == 0:
                stack.append(s[i])
            else:
                #peek, if it corresponds to current item, pop and continue
                peek = stack[-1]
                if peek == '[' and s[i] == ']':
                    stack.pop()
                elif peek == '(' and s[i] == ')':
                    stack.pop()
                elif peek == '{' and s[i] == '}':
                    stack.pop()
                else:
                    # if it doesnt, push current item
                    stack.append(s[i])                  
            i = i + 1

        # if stack is empty, return true
        if len(stack) == 0:
            return True
        # else return false
        else:
            return False