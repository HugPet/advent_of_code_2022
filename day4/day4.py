
def is_fully_within(elf_1, elf_2):
    a, b = [int(elem) for elem in elf_1]
    x, y = [int(elem) for elem in elf_2]
    if (a <= x and b >= y) or (a >= x and b <= y):
        return 1
    return 0

def is_partly_within(elf_1, elf_2):
    a, b = [int(elem) for elem in elf_1]
    x, y = [int(elem) for elem in elf_2]
    if (a <= x and b >= x) or (a <= y and b >= y) or (is_fully_within(elf_1, elf_2) == 1):
        return 1
    return 0

# 431
def day4_a():
    with open('input.txt') as f:
        input = f.readlines()
    sum = 0
    for line in input:
        pairs = line.split(",")
        sum += is_fully_within(pairs[0].split("-"), pairs[1].split("-"))
    print(sum)

# 823
def day4_b():
    with open('input.txt') as f:
        input = f.readlines()
    sum = 0
    for line in input:
        pairs = line.split(",")
        sum += is_partly_within(pairs[0].split("-"), pairs[1].split("-"))
    print(sum)  

if __name__ == "__main__":
    day4_b()