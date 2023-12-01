with open("datasets/1.1.txt") as one:
    firstNum: list = []
    secondNum: list = []
    for i, line in enumerate(one):
        for char in line:
            try:
                int(char)
                firstNum.append(char)
                break
            except Exception:
                continue
        for char in line[::-1]:
            try:
                int(char)
                secondNum.append(char)
                break
            except Exception:
                continue
    sums_list: list = zip(firstNum, secondNum)

    def sums(x, y):
        return x + y

    sums = map(sums, firstNum, secondNum)

    answer: list = []
    for i in sums:
        answer.append(int(i))
    print(sum(answer))
