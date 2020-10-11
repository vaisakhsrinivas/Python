def maxSubArray(nums):


    maxsum = nums[0]

    currentsum = nums[0]

    for i in nums[1:]:

        currentsum =  max(i, currentsum+i)
        maxsum = max(maxsum, currentsum)

    return maxsum






nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))