import typing as tp
import dataclasses
from collections import defaultdict


@dataclasses.dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_horizontal_or_vertical(self):
        return self.x1 == self.x2 or self.y1 == self.y2


class Diagram:
    def __init__(self):
        self.table = defaultdict(lambda: defaultdict(int))

    def add_straight(self, line: Line):
        for x in range(min(line.x1, line.x2), max(line.x1, line.x2) + 1):
            for y in range(min(line.y1, line.y2), max(line.y1, line.y2) + 1):
                self.table[x][y] += 1

    def add_all(self, line: Line):
        if line.is_horizontal_or_vertical():
            self.add_straight(line)
        else:
            x = line.x1
            y = line.y1
            while x != line.x2:
                self.table[x][y] += 1
                if x <= line.x2:
                    x += 1
                else:
                    x -= 1
                if y <= line.y2:
                    y += 1
                else:
                    y -= 1
            self.table[line.x2][line.y2] += 1

    def at_least(self, limit):
        res = 0
        for x, ys in self.table.items():
            for y, value in ys.items():
                if value >= limit:
                    res += 1
        return res


def get_lines(lines):
    res = []
    for line in lines:
        p1, p2 = line.split(" -> ")
        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")
        res.append(Line(int(x1), int(y1), int(x2), int(y2)))
    return res


def task1(file_name):
    lines = get_lines(open(file_name).readlines())
    diagram = Diagram()
    for line in lines:
        if line.is_horizontal_or_vertical():
            self.add_straight(line)
    return diagram.at_least(2)


def task2(file_name):
    lines = get_lines(open(file_name).readlines())
    diagram = Diagram()
    for line in lines:
        diagram.add_all(line)
    return diagram.at_least(2)
