def sort(nums):

    for i in range (len(nums)-1):
        for j in range(0, len(nums)-1-i,1):
            if nums[j] > nums[j+1]:
                swap(nums, j, j+1)

    return nums


def swap(nums, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t


if __name__ == "__main__":

    a = [4,7,9,2,4,1,3,10]
    print(sort(a))
