# # Get unique characters from a file
# with open("datasets/3.1.txt") as f:
#     unique_chars: list = []
#     for line in f:
#         for char in line:
#             if char != ".":
#                 try:
#                     int(char)
#                     continue
#                 except Exception:
#                     if char not in unique_chars:
#                         unique_chars.append(char)
#     print(unique_chars)

# Get length of each line in a file
# with open("datasets/test.txt") as f:
#     for i, line in enumerate(f):
#         print(i)
#         print(len(line))

# Get answer to 3.1
# with open("datasets/test.txt") as f:
with open("datasets/3.1.txt") as f:
    chars: list = ["/", "*", "&", "+", "$", "-", "%", "=", "@", "#"]

    nums_total: list = []
    num_positions_total: list = []
    char_positions_total: list = []
    for i, line in enumerate(f):
        num: str = ""
        nums: list = []
        num_positions: list = []
        char_positions: list = []
        for j, c in enumerate(line):
            try:
                int(c)
                num += c
            except Exception:
                if len(num) > 0:
                    nums.append([int(num)])
                    num_positions.append([j - len(num), j - 1])
                num = ""
                for char in chars:
                    if c == char:
                        char_positions.append(j)
                        break
                continue

            if j == len(line) - 1 and len(num) > 0:
                nums.append([int(num)])
                num_positions.append([j - len(num) + 1, j])

        nums_total.append(nums)
        num_positions_total.append(num_positions)
        char_positions_total.append(char_positions)
    # print(nums_total)
    # print(num_positions_total)
    # print(char_positions_total)

    nums_final: list = []
    for i, nums in enumerate(nums_total):
        nums_dict: list = []
        for j, num in enumerate(nums):
            nums_dict.append(num)
            nums_dict.append(num_positions_total[i][j])
        nums_final.append(nums_dict)

    # print(nums_final)

    valid_nums: list = []
    for i, lists in enumerate(nums_final):
        # print(lists)
        for j, list in enumerate(lists):
            # print(list)
            if len(list) == 2:
                if list[0] == 0:
                    min = 0
                else:
                    min = list[0] - 1

                if list[1] == len(line) - 1:
                    max = list[1]
                else:
                    max = list[1] + 1

                if i == 0:
                    pass
                else:
                    for char in char_positions_total[i - 1]:
                        if (char >= min) & (char <= max):
                            valid_nums.append(lists[j - 1][0])
                            break

                for char in char_positions_total[i]:
                    if (char >= min) & (char <= max):
                        valid_nums.append(lists[j - 1][0])
                        break

                if i == len(nums_total) - 1:
                    pass
                else:
                    for char in char_positions_total[i + 1]:
                        if (char >= min) & (char <= max):
                            valid_nums.append(lists[j - 1][0])
                            break

    print(sum(valid_nums))
