# 66487
def day1_a():
    with open('input.txt') as f:
        input = f.readlines()
    num_elem = input.count("\n") + 1
    arr = [0] * num_elem
    i = 0
    for line in input:
        if line == "\n":
            i += 1
            continue
        arr[i] = arr[i] + int(line)
    arr.sort(reverse=True)
    print(arr[0])

# 197301
def day1_b():
    with open('input.txt') as f:
        input = f.readlines()
    num_elem = input.count("\n") + 1
    arr = [0] * num_elem
    i = 0
    for line in input:
        if line == "\n":
            i += 1
            continue
        arr[i] = arr[i] + int(line)
    arr.sort(reverse=True)
    sum = 0
    for j in range(3):
        sum += arr[j]
    print(sum)

if __name__ == "__main__":
    day1_b()