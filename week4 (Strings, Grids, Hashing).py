# Longest Palindromic substring

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Note:
# Sliding window needs a rule where "invalid" reliably means "shrink."
# For palindromes, "invalid right now" doesn't mean shrink — it might mean grow more. So there's no reliable rule, and sliding window can't be used.

# Ex. "abaxaba"

# window "aba"    → IS a palindrome 
# add next char → "abax" → NOT a palindrome 
# Now what? Sliding window logic says "invalid → shrink from the left." So you'd shrink "abax" → "bax" → "ax"...

# But the actual longest palindrome is "abaxaba" — the whole thing!


# The right approach: Expand From Center
# "Center" means the center of the palindrome we're currently testing, not the center of given s.

def longestPalindrome(s):
    result = ""

    def expand(left, right):
        while left >=0 and right < len(s) and s[left]== s[right]:
            left -= 1       # shifting from the middle
            right += 1
        return s[left + 1 : right]  # slicing

    for i in range(len(s)):
        odd = expand(i, i)      # resulted string increasing gradually. once we get odd, then other time we get even..continue
        even = expand(i, i + 1)

        if len(odd) > len(result):
            result = odd
        if len(even) > len(result):
            result = even
    return result

print(longestPalindrome("babad"))

# why returning left + 1?
# left=-1, right=3 → left < 0 → STOP 
# Now left = -1 and right = 3

# In Python slicing s[a:b], the end b is EXCLUSIVE (it stops before b