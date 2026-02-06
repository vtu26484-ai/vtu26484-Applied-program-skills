class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0  # Pointer for popped array

        for val in pushed:
            stack.append(val)
            # Pop from stack if top matches popped[j]
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        # If stack is empty, the sequences are valid
        return not stack

        