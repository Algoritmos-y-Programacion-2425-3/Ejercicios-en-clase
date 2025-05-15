nums = [1,1,1,1]
pair_counter = 0
for index1 in range(len(nums)):
    for index2 in range(index1 + 1, len(nums)):
        if nums[index1] == nums[index2]:
            pair_counter += 1

print(pair_counter)