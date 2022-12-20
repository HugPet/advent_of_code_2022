
def find_common_a(compartment_1: str, compartment_2: str):
    for char_a in compartment_1:
        for char_b in compartment_2:
            if char_a == char_b:
                return char_a

def find_common_b(rucksack_1, rucksack_2, rucksack_3):
    for char_a in rucksack_1:
        for char_b in rucksack_2:
            if char_a != char_b:
                continue
            for char_c in rucksack_3:
                if char_a == char_c:
                    return char_a
            

def find_value(char: str):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

# 8349
def day3_a():
    with open('input.txt') as f:
        input = f.readlines()
    sum = 0
    for line in input:
        total_num = len(line)
        compartment_1 = line[:(total_num//2)]
        compartment_2 = line[(total_num//2):]
        common_char = find_common_a(compartment_1, compartment_2)
        sum += find_value(common_char)
    print(sum)

# 2681                  
def day3_b():
    with open('input.txt') as f:
        input = f.readlines()
    sum = 0
    for i in range(0, len(input), 3):
        common_char = find_common_b(input[i], input[i+1], input[i+2])
        sum += find_value(common_char)
    print(sum)

if __name__ == "__main__":
    day3_b()