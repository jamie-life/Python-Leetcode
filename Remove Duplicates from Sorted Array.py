nums = [1,1,2]

temp_dict = {}
for number in nums:
    temp_dict[number] = temp_dict.get(number, 0) + 1

unique_list = []

for key in temp_dict.keys():
    unique_list.append(key)
nums[:] = unique_list
print(nums)
