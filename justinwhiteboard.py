# You will be given an array and a limit value. You must check that all values 
# in the array are below or equal to the limit value. If they are, return True. 
# Else, return False.

#Examples
#Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], limit_value = 10
#Output = True 
#Explanation = All #s in the array are less than the limit value of 10

# You can assume all values in the array are numbers.

def array_of_limit(nums, limit_value):
    for num in nums:
        if num > limit_value:
            return("False")
    return("True")
print(array_of_limit([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10))