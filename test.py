
nums = [2, 7, 11, 15]
target = 9
hash_table = {}
for i in range(len(nums)):
        if nums[i] in hash_table:
            #print([hash_table[nums[i]], i])
            print(hash_table)
        else:
            hash_table[target - nums[i]] = i
            print(hash_table)