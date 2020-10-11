def maxSubArray(nums):


    maxsum = 0

    currentsum = 0

    for i in range(0, len(nums)):

        currentsum = currentsum + nums[i]

        if maxsum < currentsum:

            maxsum = currentsum

        elif currentsum < 0:

            currentsum = 0


    return maxsum






nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))