import math  # Needed for solution 1


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Solution 3 - After Video

        # To Solve -> https://www.youtube.com/watch?v=bNvIQI2wAjk 
        # To solve, we can iterate over the nums array twice, forward and backward, calculating
        # the prefix product and postfix product each time, and storing it directly in the res list.
        # On the first loop through, prefix begins as 1, is stored in the first index of res, and
        # prefix is then multiplied by the current index value. The same is true in reverse for the 
        # second loop through except the res list index is multiplied instead of simply stored via assignment


        res = [1] * len(nums) # create result list the length of nums

        prefix = 1 # default prefix set to 1
        for i in range(len(nums)): # iterate the nums list forward
            res[i] = prefix # set the result list index to the prefix
            prefix *= nums[i] # multiply the prefix by the index value of nums to increase

        postfix = 1 # default postfix set to 1
        for i in range(len(nums)-1, -1, -1): # iterate the nums list in reverse, going to the -1 place as to account for the 0 index
            res[i] *= postfix # multiply result list index by current postfix (note this is starting at the end of the result list)
            postfix *= nums[i] # multiply the postfix by the index value of nums to increase
            
        return res # return the result list


        # Solution 2 - Partial Video - heard the solution and thought I could implement
        # FAILED -> Also exceeds time limit of testcase 18 but is a valid and working solution to solve
        
        # ans = []

        # for i in range(len(nums)):
        #     pre = math.prod(nums[:i])
        #     post = math.prod(nums[i+1:])
        #     prod = pre * post
        #     ans.append(prod)

        # return ans




        # Solution 1 - No video 
        # FAILED -> exceeds time limit of testcase 18

        # To solve, create an answer list, then iterate len(nums)-1 time and for each iteration
        # create a tmp_list where the current index is 1. Take the product of the list and
        # store it as the value for answer[i]

        # ans = [] # empty answer list

        # for i in range(len(nums)): # iterate the len of nums
        #     tmp_list = nums.copy() # create a tmp_list of the nums list
        #     tmp_list[i] = 1 # update current index to 1
        #     product = math.prod(tmp_list) # calculate product
        #     ans.append(product) # append product to answer list

        # return ans # return answer list