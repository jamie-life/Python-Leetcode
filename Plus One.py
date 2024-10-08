# print (123 % 10)
# a = 123 % 10
# b = 123 / 10
# print(b % 10)
# c = (b / 10)
# print(c % 10)


class Solution:
    def plusOne(self, digits):
        # num = int(''.join(map(str, digits))) + 1
        # print(num)

        # temp_list = list(map(int, str(int(''.join(map(str, digits))) + 1)))
        # print(temp_list)
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))


print(Solution().plusOne([9]))