class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # To solve, we are going to store the count of each letter in a list
        # and use that list as a key for each anagram set in the given lists.
        # Storing each given anagram str to the key containing its count of letters

        res = defaultdict(list) 
            # defaultdict makes the default value of all keys the type passed

        for s in strs: # iterate over all strs

            count = [0] * 26 # create a list of 26 zeros to hold the count of each letter in the str

            for c in s: # iterate over all chars
                count[ord(c) - ord('a')] += 1 # increment the count of the char
                    # ord() provides the unicode value of the provided char
                    # to set the count of letter 'e', the index of 'e' in our list
                    # is equal to ord('e') - ord('a') --> 84 - 80 = 4 so count[4]

            res[tuple(count)].append(s) # append the str to the anagram key
                # defaultdict handled setting the default value of the key
                # if not exist, to an empty list, so .append() can be used

        return res.values()
            # The desired result is a list of lists containing the anagram pairs
            # which can be achieved via res.values() since the value of each key is a list