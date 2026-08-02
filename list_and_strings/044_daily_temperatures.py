# SOURCE: Leetcode
# https://leetcode.com/problems/daily-temperatures/
# Solution: https://neetcode.io/solutions/daily-temperatures

# Brute force solution
# Time Complexity (TC): O(n2): Because we are using a nested loop
# Space Complexity (SC): O(n): additional memory for result list
# Approach: For each temperature, iterate through the remaining temperatures to its right to
# find the next higher temperature and once found, compute the difference of those indices.
def daily_temperatures_1(temperatures):
    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                res[i] = j - i
                break
    return res


# Monotonic stack solution
# Time Complexity (TC): O(n): Because we are using a nested loop
# Space Complexity (SC): O(n): additional memory for stack and result list
# Approach: Traverse the temperatures while maintaining a monotonic stack of non-increasing order,
# compare top of the stack with current temperature. If current temperature is warmer(bigger),
# it means we have found the next warmer day for the value stored at the top of stack.
# Remove that value and calculate difference between the current and removed index. Continue popping
# until the current temperature is no longer warmer than the temperature at the top of the stack.
def daily_temperatures_2(temperatures):
    res = [0] * len(temperatures)
    stack = []  # pair: [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stack_temp, stack_idx = stack.pop()
            res[stack_idx] = i - stack_idx
        stack.append((t, i))
    return res

