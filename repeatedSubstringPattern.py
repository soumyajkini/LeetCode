def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    l = len(s)
    i = l / 2.0 # size of substring

    while(i >= 1): # check until size of substring is 1
        if (l % i == 0): # check if substring repeats multiple times
            
