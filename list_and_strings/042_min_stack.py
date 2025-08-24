# SOURCE: Leetcode
# https://leetcode.com/problems/min-stack/description/
# Solution: https://neetcode.io/solutions/min-stack


# Augmented DS technique:
# An augmented data structure is a basic data structure (like a tree, stack, queue, or heap) that has been
# enhanced with extra information to support additional operations more efficiently.
# Time Complexity (TC): O(1) for all operations.
# Space Complexity (SC): O(n)
# Approach: Use a single stack but every index will contain a dict of value and min_value
class MinStack1(object):

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.min = min(self.min, val)
        item = {'val': val, 'min': self.min}
        self.stack.append(item)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        if self.stack:
            item = self.stack[-1]
            self.min = item['min']
        else:
            self.min = float('inf')

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            item = self.stack[-1]
            return item['val']

    def getMin(self):
        """
        :rtype: int
        """
        item = self.stack[-1]
        return item['min']


# Auxiliary Stack
# Time Complexity (TC): O(1) for all operations.
# Space Complexity (SC): O(n)
# Approach: Use another stack to keep track of min values -> Pop from both in pop operation ->
# At every level of stack, it'll keep track of min value
class MinStack2(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Augmented DS technique:
# An augmented data structure is a basic data structure (like a tree, stack, queue, or heap) that has been
# enhanced with extra information to support additional operations more efficiently.
# Time Complexity (TC): O(1) for all operations.
# Space Complexity (SC): O(n)
# Approach: Use a single stack but every index will contain tuple of val, min_value
class MinStack3:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.stack[-1][1] if self.stack else val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
