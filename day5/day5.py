def get_results(stack):
    res = ""
    for string in stack:
        res += string[0]
    return res

def assemble_stacks(lines):
    stack = [""]*9
    for line in lines:
        index = 0
        while index < 9:
            if line[4*index] == "[":
                print(len(line), index)
                stack[index] += line[4*index + 1]
            index += 1
    return stack

def reveal_instructions(line: str):
    split = line.split(" ")
    no = int(split[1])
    x1 = int(split[3]) - 1
    x2 = int(split[5]) - 1
    return no, x1, x2

def execute_moves_a(stack, no, x1, x2):
    while no > 0:
        move_char = stack[x1][0]
        stack[x1] = stack[x1][1:]
        stack[x2] = move_char + stack[x2]
        no -= 1
    return stack

def execute_moves_b(stack, no, x1, x2):
    move_chars = stack[x1][0:no]
    stack[x1] = stack[x1][no:]
    stack[x2] = move_chars + stack[x2]
    return stack

# WCZTHTMPS
def day5_a():
    with open('input.txt') as f:
        input = f.readlines()
    i = 0
    while input[i] != " 1   2   3   4   5   6   7   8   9 \n":
        i += 1
    stack = assemble_stacks(input[:i])
    for line in input:
        if line[:4] != "move":
            continue
        no, x1, x2 = reveal_instructions(line)
        stack = execute_moves_a(stack, no, x1, x2)
    print(stack)
    print(get_results(stack))

# BLSGJSDTS
def day5_b():
    with open('input.txt') as f:
        input = f.readlines()
    i = 0
    while input[i] != " 1   2   3   4   5   6   7   8   9 \n":
        i += 1
    stack = assemble_stacks(input[:i])

    for line in input:
        if line[:4] != "move":
            continue
        no, x1, x2 = reveal_instructions(line)
        stack = execute_moves_b(stack, no, x1, x2)
    print(stack)
    print(get_results(stack))

if __name__ == "__main__":
    day5_b()