with open("datasets/2.1.txt") as d:
    power_list: list = []
    for i, v in enumerate(d):
        color_count = {"red": 0, "green": 0, "blue": 0}

        d1 = v.split(":")[1].split(";")

        any_invalid = False
        for s in d1:
            for color in color_count.keys():
                if color in s:
                    # Get index of color
                    int_index = s.index(color) - 3
                    color_int = int(s[int_index : int_index + 2].strip())

                    if color_int > color_count[color]:
                        color_count[color] = color_int
        print(color_count)
        # print(f"{color}:{color_count[color]}")

        append_val = 1
        for color, lowest_v in color_count.items():
            append_val *= lowest_v
            print(append_val)
        power_list.append(append_val)
        print(power_list)
    print(sum(power_list))
