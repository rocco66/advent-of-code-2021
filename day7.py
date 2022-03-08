import math


def find(crabs):
    min_fuel = None
    for hyp in range(min(crabs), max(crabs) + 1):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab - hyp)
        if min_fuel is None or fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


def find2(crabs):
    min_fuel = None
    for hyp in range(min(crabs), max(crabs) + 1):
        fuel = 0
        for crab in crabs:
            for s in range(abs(crab - hyp) + 1):
                fuel += s
        print(f"hyp={hyp} fuel={fuel}")
        if min_fuel is None or fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


def task1(file_name):
    crabs = []
    for line in open(file_name):
        crabs += [int(t) for t in line.split(",")]
    print(find(crabs))


def task2(file_name):
    crabs = []
    for line in open(file_name):
        crabs += [int(t) for t in line.split(",")]
    print(find2(crabs))
