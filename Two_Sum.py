# Question Name: Two Sum
# Difficuly level: EASY

# Question prompt: 
    # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    # You may assume that each input would have exactly one solution, and you may not use the same element twice.
    # You can return the answer in any order.

# Question Intuition: 
    # Given an array of lists => can access all elements using for loop;
    # Since we need two numbers => possibly need two for loops to act as pointers
    # At the end of all i + j combinations we should have our answer. Or No Answer

# SOLUTION 1 : Hit and trial of all i + j possibilities

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first number 
        for i in range(0, len(nums) - 1):
        # second number
            for j in range(i + 1, len(nums) ):
        # trial and error of all possible solutions and check if they match target
                if nums[i] + nums[j] == target:
                    return [i,j]


# SOLUTION 2 : Using Dictionary

# Everytime you come across a number save the "need" i.e the other number needed with it to reach target.
# Then continue moving along the array if you come across a number that is equal to a 
# "need" of a previous number we have our answer, else store the need of that number in the dictionary.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==1: return 0
        mem = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if nums[i] not in mem:
                mem[need] = i
            else:
                return[mem[nums[i]],i]

