# SOURCE: Leetcode
# https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1747561031/
# Solution: https://neetcode.io/solutions/evaluate-reverse-polish-notation


# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
# Approach: use a stack -> if number -> push on stack -> if operator -> pop its operands -> push result on stack
def evalRPN_1(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    operator_map = {
        "+": lambda l, r: l + r,
        "*": lambda l, r: l * r,
        "-": lambda l, r: l - r,
        "/": lambda l, r: int(l / r),
    }

    for token in tokens:
        if token in operator_map:
            right = stack.pop()
            left = stack.pop()
            token = operator_map[token](left, right)
        stack.append(int(token))

    return stack.pop()


# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)
# Approach: use a stack -> if number -> push on stack -> if operator -> pop its operands -> push result on stack
def evalRPN_2(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    operators = ('+', '-', '*', '/')
    for t in tokens:
        if t in operators:
            op2 = stack.pop()
            op1 = stack.pop()

            if t == '+':
                result = op1 + op2
            elif t == '-':
                result = op1 - op2
            elif t == '*':
                result = op1 * op2
            else:
                result = int(op1 / op2)
            stack.append(result)
        else:
            stack.append(int(t))

    return stack.pop()
