
def unique(sub_str: str):
    for i in range(len(sub_str)):
        current_char = sub_str[i]
        if sub_str.count(current_char) >= 2:
            return False
    return True

def find_n_different(input: str, n):
    index = 0
    while index - n < len(input):
        sub_str = input[index:index+n]
        print(sub_str)
        if unique(sub_str):
            return index+n
        index += 1

# 1804
def day6_a():
    with open('input.txt') as f:
        input = f.readlines()
    print(find_n_different(input[0], 4))

# 2508
def day6_b():
    with open('input.txt') as f:
        input = f.readlines()
    print(find_n_different(input[0], 14))

if __name__ == "__main__":
    day6_b()