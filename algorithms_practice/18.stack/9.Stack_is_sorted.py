"""
Given a stack, a function is_sorted accepts a stack as a parameter and returns
true if the elements in the stack occur in ascending increasing order from
bottom, and false otherwise. That is, the smallest element should be at bottom
For example:
bottom [6, 3, 5, 1, 2, 4] top
The function should return false
bottom [1, 2, 3, 4, 5, 6] top
The function should return true
"""
from algorithms.stack import is_sorted

bottom=[6, 3, 5, 1, 2, 4]
bottom2= [1, 2, 3, 4, 5, 6]


print(is_sorted(bottom))


print(is_sorted(bottom2))