
class Map:

    MAX_ENERGY = 9

    def __init__(self, m):
        self._m = m
        self._max_y = len(m) - 1
        self._max_x = len(m[0]) - 1
        self.flash_count = 0

    def _tick(self):
        flashed = set()
        current_stack = []
        for y, xs in enumerate(self._m):
            for x, val in enumerate(xs):
                self._m[y][x] += 1
                if self._m[y][x] == MAp.MAX_ENERGY:
                    flashed.add(pos)
                    current_stack.append(pos)
                if y > 0:
                    current_stack.append((y - 1, x))
                    if x > 0:
                        current_stack.append((y - 1, x - 1))
                if y != max_y:
                    current_stack.append((y + 1, x))
                    if x != max_x:
                        current_stack.append((y + 1, x + 1))
                if x > 0:
                    current_stack.append((y, x - 1))
                if x != max_x:
                    current_stack.append((y, x + 1))

    def simulate(self, count):
        for _c in range(count):
            self._tick()


def task1(file_name):
    rows = []
    for line in open(file_name):
        rows.append([int(c) for c in line[:-1]])
    m = Map(rows)
    m.simulate(100)
    print(m.flash_count)
