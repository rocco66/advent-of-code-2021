import typing as tp
import dataclasses

@dataclasses.dataclass
class Board:
    table: list[list[int]]
    rows: list[int]
    columns: list[int]

    def check(self, num) -> bool:
        for r_i in range(5):
            for c_i in range(5):
                if self.table[r_i][c_i] == num:
                    self.rows[r_i] += 1
                    self.columns[c_i] += 1
                    if self.rows[r_i] == 5 or self.columns[c_i] == 5:
                        return True

    def get_winner_numbers(self, found_numbers):
        for r_i in range(5):
            for c_i in range(5):
                if self.table[r_i][c_i] not in found_numbers:
                    yield self.table[r_i][c_i]


def get_randoms(lines):
    return [int(n) for n in lines[0].split(",")]


def get_boards(lines):
    res = []
    for i in range(2, len(lines), 6):
        table = []
        for l in range(5):
            table.append([int(t) for t in lines[i + l].split(" ") if t])
        res.append(Board(table, [0]* 5, [0] * 5))
    return res


def task1(file_name):
    lines = open(file_name).readlines()
    randoms = get_randoms(lines)
    boards = get_boards(lines)
    found_nums = set()
    for n in randoms:
        found_nums.add(n)
        for board in boards:
            if board.check(n):
                return n * sum(board.get_winner_numbers(found_nums))


def task2(file_name):
    lines = open(file_name).readlines()
    randoms = get_randoms(lines)
    boards = get_boards(lines)
    found_nums = set()
    wons_boards = set()
    for n in randoms:
        found_nums.add(n)
        for board in boards:
            if board.check(n):
                wons_boards.add(id(board))
                if len(wons_boards) == len(boards):
                    return n * sum(board.get_winner_numbers(found_nums))
