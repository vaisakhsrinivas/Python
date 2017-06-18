def sort(nums):

    for i in range (len(nums)):
        j = i

        while j>0 and nums[j-1] > nums[j]:
            swap(nums, j, j-1)
            j = j-1

    return nums


def swap(nums, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t

if __name__ == "__main__":

    a = [4,7,9,2,4,1,3,10]
    print(sort(a))