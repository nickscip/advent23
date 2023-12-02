with open("datasets/2.1.txt") as d:
    possible_games: list = []
    for i, v in enumerate(d):
        color_count = {"red": 12, "green": 13, "blue": 14}

        d1 = v.split(":")[1].split(";")

        any_invalid = False
        for s in d1:
            for color in color_count.keys():
                if color in s:
                    # Get index of color
                    int_index = s.index(color) - 3
                    color_int = int(s[int_index : int_index + 2].strip())

                    if color_int <= color_count[color]:
                        continue
                    else:
                        any_invalid = True
                        break
            if any_invalid:
                break
        if not any_invalid:
            possible_games.append(i + 1)
    print(sum(possible_games))
