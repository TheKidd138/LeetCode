def group_anagrams(strs):

    anagram_groups = {}
    for s in strs:
        comped = ''.join(sorted(s))
        if comped in anagram_groups:
            temp = anagram_groups[comped]
            temp.append(s)
            anagram_groups[comped] = temp
        else:
            anagram_groups[comped] = [s]

    grouped = []
    for key in anagram_groups.keys():
        if grouped:
            grouped.append(anagram_groups[key])
        else:
            grouped = [anagram_groups[key]]

    return grouped

    ## This didnt work because it returns the grouped anagrams as their dictionary form
    # anagrams_groups = []
    # for s in strs:
    #     entry = {}
    #     for c in s:
    #         if c not in entry:
    #             entry[c] = 1
    #         else:
    #             entry[c] += 1

    #     if anagrams_groups:
    #         for i, groups in enumerate(anagrams_groups):
    #             if entry in groups:
    #                 groups.append(entry)
    #                 anagrams_groups[i] = groups
    #             else:
    #                 anagrams_groups.append([entry])
    #     else:
    #         anagrams_groups.append([entry])

    # return anagrams_groups


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


solved = group_anagrams(strs)

print(solved)
