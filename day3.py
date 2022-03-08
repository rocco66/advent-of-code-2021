
def task1(file_name):
    bits_count = [0] * 12
    lines = open(file_name).readlines()
    for value_str in lines:
        for bit_position in range(-1, -13, -1):
            bits_count[bit_position] += int(value_str[bit_position - 1])
    gamma_ray_bits = [1 if b > len(lines) / 2 else 0 for b in bits_count]
    epsilon_ray_bits = [0 if b > len(lines) / 2 else 1 for b in bits_count]
    gamma_ray = int("".join(str(b) for b in gamma_ray_bits), base=2)
    epsilon_ray = int("".join(str(b) for b in epsilon_ray_bits), base=2)
    return gamma_ray * epsilon_ray



def _find(lines, keep_pred):
    for bit_position in range(0, 12):
        ones_count = 0
        for value_str in lines:
            ones_count += int(value_str[bit_position])
        print(f"* bit_position={bit_position} ones_count={ones_count}, lines_count={len(lines)} lines {', '.join(lines)}")
        lines = [l for l in lines if keep_pred(l[bit_position], ones_count, len(lines))]
        if len(lines) == 1:
            return int(lines[0], base=2)


def find_oxygen(lines):
    def pred(current, ones_count, lines_count):
        if ones_count >= (lines_count / 2):
            return current == "1"
        else:
            return current == "0"

    return _find(lines, pred)


def find_co2(lines):
    def pred(current, ones_count, lines_count):
        if ones_count >= (lines_count / 2):
            return current == "0"
        else:
            return current == "1"
    return _find(lines, pred)


def task2(file_name):
    lines = [l[:-1] for l in open(file_name).readlines()]
    return find_oxygen(lines) * find_co2(lines)
