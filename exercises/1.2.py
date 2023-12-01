with open("datasets/1.1.txt") as one:
    decoder: dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    firstNum: list = []
    secondNum: list = []
    for i, line in enumerate(one):
        numWord1: list = []
        for char in line:
            try:
                int(char)
                firstNum.append(char)
                break
            except Exception:
                numWord1.append(char)
                for key in decoder.keys():
                    if key in "".join(numWord1):
                        firstNum.append(decoder[key])
                        break
                    else:
                        continue
            if len(firstNum) == i + 1:
                break
            else:
                continue
        numWord2: list = []
        for char in line[::-1]:
            try:
                int(char)
                secondNum.append(char)
                break
            except Exception:
                numWord2.append(char)
                numWord2rev = numWord2[::-1]
                for key in decoder.keys():
                    if key in "".join(numWord2rev):
                        secondNum.append(decoder[key])
                        break
                    else:
                        continue
            if len(secondNum) == i + 1:
                break
            else:
                continue
    sums_list: list = zip(firstNum, secondNum)

    def sums(x, y):
        return x + y

    sums = map(sums, firstNum, secondNum)

    answer: list = []
    for i in sums:
        answer.append(int(i))
    print(sum(answer))
