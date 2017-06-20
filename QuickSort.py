def qsort(nums,low,high):
    if low >= high:
        return

    p = partition(nums, low, high)
    qsort(nums, low, p-1)
    qsort(nums, p+1, high)

def partition(nums, low, high):
    index = (low+high)//2
    swap(nums, index, high)

    i = low

    for j in range(low, high,1):
        if nums[j] <= nums[high]:
            swap(nums, i, j)
            i = i+1

    swap(nums, i, high)
    return i

def swap(nums, i, j):
    t = nums[i]
    nums[i]= nums[j]
    nums[j] = t


if __name__ == "__main__":

    nums=[-3,5,3,2,0,9,1]
    qsort(nums, 0, len(nums)-1)
    print(nums)