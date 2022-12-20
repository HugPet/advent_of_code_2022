
winner_dict_a = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,

    "B X": 0,
    "B Y": 3,
    "B Z": 6,

    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}

picker_dict_a = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

winner_dict_b = {
    "A X": "Z",
    "A Y": "X",
    "A Z": "Y",

    "B X": "X",
    "B Y": "Y",
    "B Z": "Z",

    "C X": "Y",
    "C Y": "Z",
    "C Z": "X",
}

# 8890
def day2_a():
    with open('input.txt') as f:
        input = f.readlines()
    sum = 0
    for line in input:
        line = line.replace("\n", "")
        sum += winner_dict_a[line] + picker_dict_a[line[2]]
    print(sum)

# 10238
def day2_b():
    with open('input.txt') as f:
        input = f.readlines()
    sum = 0
    for line in input:
        line = line.replace("\n", "")
        line = line[0:2] + winner_dict_b[line]
        sum += winner_dict_a[line] + picker_dict_a[line[2]]
    print(sum)


if __name__ == "__main__":
    day2_b()