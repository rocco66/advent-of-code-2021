PAIRS = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}

CORRUPED_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


INCOMPLETE_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def find_first_illegal_char(line):
    stack = []
    for i, char in enumerate(line):
        if char in PAIRS:
            stack.append(char)
        else:
            prev_char = stack.pop()
            if PAIRS[prev_char] != char:
                return char


def find_incomplete_chars(line):
    stack = []
    for i, char in enumerate(line):
        if char in PAIRS:
            stack.append(char)
        else:
            prev_char = stack.pop()
            if PAIRS[prev_char] != char:
                return
    res = [PAIRS[c] for c in stack][::-1]
    return res


def calculate_incomplete_scores(line):
    res = 0
    for c in line:
        res = res * 5 + INCOMPLETE_SCORES[c]
    return res


def task1(file_name):
    illegal_chars = []
    for line in open(file_name):
        if illegal_char := find_first_illegal_char(line[:-1]):
            illegal_chars.append(illegal_char)
    print(sum(CORRUPED_SCORES[c] for c in illegal_chars))


def task2(file_name):
    incomplete_lines = []
    for line in open(file_name):
        if incomplete_chars := find_incomplete_chars(line[:-1]):
            incomplete_lines.append(incomplete_chars)

    scores = [calculate_incomplete_scores(l) for l in incomplete_lines]
    scores.sort()
    print(scores[int(len(scores) / 2)])


