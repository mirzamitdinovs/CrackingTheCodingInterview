# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

#Version 1 with additional Space
def isUnique(s)-> bool:
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True

# Time Complexity: O(n)
# Space Complexity: O(n)


#Version 2 without additional Space

def isUnique(s)->bool:
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i]==s[j]:
                return False
    return True

# Time Complexity: O(n2)
# Space Complexity: O(1)
