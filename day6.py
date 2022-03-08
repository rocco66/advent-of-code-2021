import typing as tp
import dataclasses
from collections import defaultdict


class FishPack:

    def __init__(self, fish):
        self.fish_types = defaultdict(int)
        for f in fish:
            self.fish_types[f] += 1

    def simulate(self, days):
        for d in range(days):
            print(f"day {d}, pack {self.fish_types}")
            newborn_count = 0
            new_fish_types = defaultdict(int)
            for fish_type, fish_count in self.fish_types.items():
                if fish_type == 0:
                    new_fish_types[6] += fish_count
                    newborn_count += fish_count
                else:
                    new_fish_types[fish_type - 1] += fish_count
            if newborn_count:
                new_fish_types[8] = newborn_count
            self.fish_types = new_fish_types

    def __len__(self):
        print(list(self.fish_types.values()))
        return sum(self.fish_types.values())


def task1(file_name):
    fish = []
    for line in open(file_name):
        fish += [int(t) for t in line.split(",")]
    pack = FishPack(fish)
    pack.simulate(80)
    print(len(pack))


def task2(file_name):
    fish = []
    for line in open(file_name):
        fish += [int(t) for t in line.split(",")]

    pack = FishPack(fish)
    pack.simulate(256)
    print(len(pack))
