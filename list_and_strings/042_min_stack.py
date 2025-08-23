# SOURCE: Leetcode
# https://leetcode.com/problems/min-stack/description/
# Solution: https://neetcode.io/solutions/min-stack


#
# Time Complexity (TC):
# Space Complexity (SC):
# Approach:
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


class MinStack2(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.min_stack.append(val)
        else:
            min_top = self.min_stack[-1]
            self.min_stack.append(min(val, min_top))
        self.stack.append(val)

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
