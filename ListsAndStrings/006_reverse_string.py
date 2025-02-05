# SOURCE: Leetcode
# https://leetcode.com/problems/reverse-string/
# Solution: https://www.youtube.com/watch?v=_d0T_2Lk2qA (Neetcode)


# Solution # 1

# Time Complexity (TC): O(n): two pointer solution
# Space Complexity (SC): O(1): in-place swapping
# Approach: Use two pointers i and j -> swap their positions
def reverse_string_1(s):
    j = len(s) - 1
    for i in range(len(s) // 2):
        s[i], s[j - i] = s[j - i], s[i]
    return s


# Solution # 2

# Time Complexity (TC): O(n): traverse the whole array
# Space Complexity (SC): O(n): using a stack which increases with input size
# Approach: Use a stack -> append each char into the stack -> stack contains reversed sequence
# -> go through each element into the stack -> pop it -> re-assign it with each element in array
def reverse_string_2(s):
    stack = []
    for char in s:
        stack.append(char)

    for i in range(len(s)):
        s[i] = stack.pop()

    return s


# Solution # 3

# Time Complexity (TC): O(n): Total no. of swaps scales linearly with n
# Space Complexity (SC): O(n): We're using space from the recursive call stack -> each
# recursive call adds a frame to the call stack and Python does not optimise tail recursion
# Approach: Recursively swaps the pair of elements starting from outermost indices
# -> for a list of n, it requires n/2 swaps -> this scales linearly with n
def reverse_string_3(s):
    def reverse(l, r):
        if l < r:
            s[l], s[r] = s[r], s[l]
            reverse(l + 1, r - 1)
        return

    reverse(0, len(s) - 1)
