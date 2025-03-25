import random

# Recursive algorithm:
#     A function calling itself.
#     A natural choice for design & conquer strategy
# Divide & Conquer Algorithm:
#     It is an algorithm design paradigm in which we break a problem into sub-problems and
#     then from the solutions to the sub-problems, we construct the solution to the actual problem
#     Mostly implemented using recursion
# Not a stable sorting algorithm:
#     In a stable sorting algo, the relative order of records with equal key is preserved. A sorting algo
#     can be used to sort a list of any data type - not just integers. In case of complex data types, we
#     sort on some property of records on some key.
#     For example: We want to sort a list of points in Cartesian plane in
#     increasing order of x co-ordinate. [(1,2), (4,5), (2,3), (4,3), (5,2)].
#     By using a stable sorted algo, point (4,5) will be before (4,3) i.e. persist its relative order.
#     Partitioning logic in Quick sort doesn't ensure stability

# Fast and efficient in practical scenarios
# Most practical choice for an efficient sorting algo.
# In fact sort functions of most lang libraries are implementations of quick sort only

# Time Complexity
# ø(nlogn) - Best + Average case
# O(n2) - Worst case: Can be almost avoided by using randomised version of quick sort

# Randomised Quick Sort: Gives us O(nlogn) running time with very high probability

# Space Complexity
# Average case: O(logn): Such small rate of growth that we can say its in-place i.e. constant
# because log n for all practical values is very small i.e. almost negligible
# Worst case: O(n)

def quick_sort(array, start, end):
    if start < end:
        p_index = random_partition(array, start, end)
        quick_sort(array, start, p_index - 1)
        quick_sort(array, p_index + 1, end)


def partition(array, start, end):
    pivot = array[end]
    p_index = start
    for i in range(start, end):
        if array[i] <= pivot:
            array[i], array[p_index] = array[p_index], array[i]
            p_index += 1
    array[end], array[p_index] = array[p_index], array[end]
    return p_index


def random_partition(array, start, end):
    pivot_index = random.randint(start, end)
    array[pivot_index], array[end] = array[end], array[pivot_index]
    return partition(array, start, end)


nums = [7, 2, 1, 6, 8, 5, 3, 4]
quick_sort(nums, 0, 7)
print(nums)
