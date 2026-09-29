class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ["{", "[", "("]
        closed_brackets = ["}", "]", ")"]
        for i in s:
            if i in open_brackets:
                stack.append(i)
            elif i in closed_brackets:
                index = closed_brackets.index(i)
                if len(stack) == 0:
                    return False
                elif stack[-1] == open_brackets[index]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
