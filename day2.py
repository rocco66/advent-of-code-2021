import dataclasses

@dataclasses.dataclass
class State:
    depth: int
    position: int
    aim: int


def task1(file_name):
    state = State(0, 0 ,0)
    for line in open(file_name):
        cmd, value_str = line.split(" ")
        value = int(value_str)
        if cmd == "forward":
            state.position += value
        elif cmd == "up":
            state.depth -= value
        elif cmd == "down":
            state.depth += value
        else:
            raise RuntimeError()
    return state.depth * state.position



def task2(file_name):
    state = State(0, 0 ,0)
    for line in open(file_name):
        cmd, value_str = line.split(" ")
        value = int(value_str)
        if cmd == "forward":
            state.position += value
            state.depth += (state.aim * value)
        elif cmd == "up":
            state.aim -= value
        elif cmd == "down":
            state.aim += value
        else:
            raise RuntimeError()
        print(f"line='{line[:-1]}' , state={state}")
    return state.depth * state.position

