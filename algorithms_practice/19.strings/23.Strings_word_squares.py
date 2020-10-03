# Given a set of words (without duplicates),
# find all word squares you can build from them.

# A sequence of words forms a valid word square
# if the kth row and column read the exact same string,
# where 0 ≤ k < max(numRows, numColumns).

# For example, the word sequence ["ball","area","lead","lady"] forms
# a word square because each word reads the same both horizontally
# and vertically.

# b a l l
# a r e a
# l e a d
# l a d y
# Note:
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.

# Example 1:

# Input:
# ["area","lead","wall","lady","ball"]

# Output:
# [
# [ "wall",
# "area",
# "lead",
# "lady"
# ],
# [ "ball",
# "area",
# "lead",
# "lady"
# ]
# ]
from algorithms.strings import word_squares

a=["area","lead","wall","lady","ball"]

print(word_squares(a))