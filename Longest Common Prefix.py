# strs = ["flower", "flow", "flight"]
# strs = ["dog","racecar","car"]
strs = ["ab", "a"]


longest_common = ""
for x in range (0, len(min(strs, key=len))):
    # print(x)
    # print(strs[2][x])
    unique_set = set(list(map(lambda y: y[0:x+1], strs)))
    if len(unique_set) == 1:
        longest_common = unique_set.pop()
    print(unique_set)

# print(min_len)
# print(spliced_list)
# print(unique_set)
print(longest_common)