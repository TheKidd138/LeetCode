###
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
###

s, t = "anagram", "nagaram"

s_dict = {}
t_dict = {}

if len(s) != len(t):
    print(False)
else:
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = 1
        else:
            s_dict[s[i]] = s_dict[s[i]] + 1
        if t[i] not in t_dict:
            t_dict[t[i]] = 1
        else:
            t_dict[t[i]] = t_dict[t[i]] + 1
if s_dict == t_dict:
    print(True)
else:
    print(False)
