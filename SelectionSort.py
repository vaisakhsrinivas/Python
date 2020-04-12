def sort(nums):

    for i in range(len(nums)-1):

        index = i

        for j in range(i+1,len(nums),1):
            if nums[j] < nums[index]:
                index = j

        if index != i:
            swap(nums, index, i)

    return nums

def swap(nums, i, j):

    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t


if __name__ == "__main__":

    nums = [5,2,1,7,6,8,0]
    print(sort(nums))


