class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Submission 2
        # To solve, we are going to implement a bucket sort algo that uses a hashmap to store
        # the count of each number and then a list as long as the nums array to store the 
        # numbers in a list (building a list of lists) where the values of the list occurred
        # the number of times as the index. Then iterating over the list of lists in reverse
        # order, appending the values from the sublist to the response until the len of response
        # is equal to k

        count = {} # empty hashmap to store ints in array nums as the key and the count as the value
        freq = [[] for i in range(len(nums) + 1)] # list of lists to store the frequency of nums at the index

        for n in nums: # iterate all the nums in the list
            count[n] = 1 + count.get(n, 0) # increment the key by one to get the count of each unique num

        for key, val in count.items(): # iterate over the items, getting the key and value
            freq[val].append(key) # store the key (or int) at the index of the count value (or frequency of occurrence)

        res = [] # empty response list for k most frequent ints
        for i in range(len(freq) - 1, 0, -1): # iterate the list of lists backwards
            for n in freq[i]: # iterate each number in the sublist
                res.append(n) # append that int to the response list
                if len(res) == k: # check if the response is equal to k
                    return res # if so, return the response



        # Submission 1

        # res = defaultdict(int) # create a defaultdict with default value int (which is 0)

        # for n in nums: # iterate over all of the nums
        #     res[n] += 1 # increment the value representing the occurence of the number (which is the key)

        # sorted_res = dict(sorted(res.items(),key = lambda item: item[1], reverse=True))
        #     # dict() will create a dictionary from the result of sorted()
        #     # sorted() sorts (duh!)
        #         # param1 -> the collection to sort
        #         #param2 (key) -> a function to apply before sorting
        #             # in this case, getting the [1] index of the items, which is the values
        #         #param2 (reverse) -> the order in which to sort

        # return list(sorted_res.keys())[:k] # get the keys of the sorted_res, taking only the first k values
            

