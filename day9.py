def find_risk_levels(m):
    risk_levels = []
    max_y = len(m) - 1
    max_x = len(m[0]) - 1
    for y, xs in enumerate(m):
        for x, current in enumerate(xs):
            if y > 0 and m[y - 1][x] <= current:
                continue
            if y != max_y and m[y + 1][x] <= current:
                continue
            if x > 0 and m[y][x - 1] <= current:
                continue
            if x != max_x and m[y][x + 1] <= current:
                continue
            risk_levels.append(current + 1)
    return risk_levels



def task1(file_name):
    map_ = []
    for line in open(file_name):
        map_.append([int(t) for t in line[:-1]])
    print(sum(find_risk_levels(map_)))


def find_basins(m):
    known_locations = set()
    basins = []
    current_basin = set()
    current_stack = []
    max_y = len(m) - 1
    max_x = len(m[0]) - 1
    for y, xs in enumerate(m):
        for x, current in enumerate(xs):
            pos = y, x
            current_stack.append(pos)
            while current_stack:
                pos = (y, x) = current_stack.pop()
                if m[y][x] == 9 or pos in known_locations:
                    if pos not in known_locations:
                        known_locations.add(pos)
                    continue
                if y > 0:
                    current_stack.append((y - 1, x))
                if y != max_y:
                    current_stack.append((y + 1, x))
                if x > 0:
                    current_stack.append((y, x - 1))
                if x != max_x:
                    current_stack.append((y, x + 1))
                known_locations.add(pos)
                current_basin.add(pos)
            basins.append(current_basin)
            current_basin = set()
    return basins




def task2(file_name):
    map_ = []
    for line in open(file_name):
        map_.append([int(t) for t in line[:-1]])
    sorted_basins = sorted(find_basins(map_), key=lambda b: len(b))
    res = 1
    for b in sorted_basins[-3:]:
        res *= len(b)
    print(res)
