from dataclasses import dataclass


@dataclass
class Elf:
    id: int
    items: list

    def item_sum(self):
        return sum(self.items)


def parse_input(puzzle_input):
    elfs = [Elf(0, [])]
    x = 0
    for index, i in enumerate(puzzle_input):
        if i != '\n':
            elfs[x].items.append(int(i))
        if i == '\n':
            x = x + 1
            elfs.append(Elf(x, []))

    elfs.sort(key=lambda elf: elf.item_sum(), reverse=True)
    return elfs
