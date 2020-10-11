def removeDuplicates(nums):


    i = 1
    count = 1


    while i < len(nums):

        if nums[i] == nums[i-1]:

            count = count + 1

            if count > 2:

                nums.pop(i)
                i = i - 1

        else:

            count = 1

        i = i + 1

    return len(nums)




nums = [0,0,1,1,1,1,2,3,3]

print(removeDuplicates(nums))