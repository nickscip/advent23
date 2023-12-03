# Get answer to 3.2
with open("datasets/3.1.txt") as f:
    chars: list = ["*"]

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

    answer: list = []
    for i, chars in enumerate(char_positions_total):
        if len(chars) > 0:
            for j, char in enumerate(chars):
                valid_nums: list = []
                if i == 0:
                    pass
                else:
                    for k, list in enumerate(nums_final[i - 1]):
                        if len(list) == 2:
                            if list[0] == 0:
                                min = 0
                            else:
                                min = list[0] - 1
                            if list[1] == len(line) - 1:
                                max = list[1]
                            else:
                                max = list[1] + 1
                            if (char >= min) & (char <= max):
                                valid_nums.append(
                                    nums_final[i - 1][
                                        nums_final[i - 1].index(list) - 1
                                    ][0]
                                )

                for k, list in enumerate(nums_final[i]):
                    if len(list) == 2:
                        if list[0] == 0:
                            min = 0
                        else:
                            min = list[0] - 1
                        if list[1] == len(line) - 1:
                            max = list[1]
                        else:
                            max = list[1] + 1
                        if (char >= min) & (char <= max):
                            valid_nums.append(
                                nums_final[i][nums_final[i].index(list) - 1][0]
                            )

                if i == len(nums_total) - 1:
                    pass
                else:
                    for k, list in enumerate(nums_final[i + 1]):
                        if len(list) == 2:
                            if list[0] == 0:
                                min = 0
                            else:
                                min = list[0] - 1
                            if list[1] == len(line) - 1:
                                max = list[1]
                            else:
                                max = list[1] + 1
                            if (char >= min) & (char <= max):
                                valid_nums.append(
                                    nums_final[i + 1][
                                        nums_final[i + 1].index(list) - 1
                                    ][0]
                                )

                if len(valid_nums) == 2:
                    answer.append(valid_nums[0] * valid_nums[1])
    print(sum(answer))
