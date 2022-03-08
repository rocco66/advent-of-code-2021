

def task1(file_name):
    res = 0
    for line in open(file_name):
        line = line[:-1]
        before_t, after_t = line.split("|")
        for digits in after_t.split(" "):
            if len(digits) in {2, 3, 4, 7}:
                print(digits)
                res += 1
        print(f"{line} : {res}")
    print(res)


class Code:
    def __init__(self):
        #  -1-
        # 0   2
        # +-3-+
        # 4   5
        #  -6-
        self.trans_map = {}

    def add_1(segments):
        self.trans_map[2] = segments[0]
        self.trans_map[5] = segments[1]

    def add_7(segments):
        self.trans_map[1] = segments[0]
        self.trans_map[2] = segments[1]
        self.trans_map[5] = segments[2]

    def add_4(segments):
        self.trans_map[0] = segments[0]
        self.trans_map[3] = segments[1]
        self.trans_map[2] = segments[2]
        self.trans_map[5] = segments[3]

    def add(segments):
        if len(segments) == 2:
            self.add_1(segments)
        elif len(segments) == 3:
            self.add_7(segments)
        elif len(segments) == 4:
            self.add_4(segments)


def decode(digits):
    code = Code()
    for segments in digits:
        code.add(segments)
    print

def task2(file_name):
    res = 0
    for line in open(file_name):
        line = line[:-1]
        before_t, after_t = line.split("|")
        code = decode(after_t.split(" "))
        for digits in before_t.split(" "):
            pass
    print(res)
