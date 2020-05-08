class Three_sum:
    def Three_sum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        threenumbers = set()
        l = len(nums)

        for i in range (l - 2):
            left = i+1
            right = l-1

            while (left < right):
                if (nums[i]+nums[left]+nums[right]) == 0:
                    threenumbers.add(tuple(sorted(nums[i], nums[left], nums[right])))
                    left = left + 1
                    right = right - 1
                elif (nums[i]+nums[left]+nums[right]) > 0:
                    right = right - 1
                else:
                    left = left + 1

        return [[x[0], x[1], x[2]] for x in threenumbers]






#n = [-1,0,1,2,-1,-4]
#result = Three_sum()
#result.Three_sum(n)