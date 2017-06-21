def merge_sort(nums):
    if len(nums) == 1:
        return

    middle = len(nums) // 2

    left = nums[:middle]
    right = nums[middle:]

    merge_sort(left)
    merge_sort(right)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right [j]:
            nums[k] = left[i]
            i = i+1
        else:
            nums[k] = right[j]
            j = j+1

        k = k+1

    while i < len(left):
        nums[k] = left[i]
        k = k + 1
        i = i + 1

    while j < len(right):
        nums[k] = right[j]
        k = k + 1
        j = j + 1

if __name__ == "__main__":

    nums = [6,3,2,-1,-2,-1]
    merge_sort(nums)
    print(nums)