def task1(file_name):
    prev = None
    res = 0
    for line in open(file_name):
        num = int(line)
        if prev is not None:
            if num > prev:
                res += 1
        prev = num
    return res


def task2(file_name):
    prev = None
    res = 0
    lines = open(file_name).readlines()
    for i in range(0, len(lines) - 2):
        num = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        if prev is not None:
            if num > prev:
                res += 1
        prev = num
        print(f"i={i}, num={num}, {lines[i: i+ 3]}")
    return res
