import puzzle_1 as p1
import puzzle_2 as p2


def get_puzzle_input(filepath):
    with open(filepath) as f:
        puzzle_input = f.readlines()

    return puzzle_input


def main():
    puzzle_input = get_puzzle_input('input_puzzle_1.txt')
    sorted_elfs = p1.parse_input(puzzle_input)
    print('1.1 Puzzle: ' + str(sorted_elfs[0].item_sum()))
    print('1.1 Puzzle: ' + str(sorted_elfs[0].item_sum() + sorted_elfs[1].item_sum() + sorted_elfs[2].item_sum()))

    puzzle_input = get_puzzle_input('input_puzzle_2.txt')
    points = p2.parse_input(puzzle_input)
    print('2.1 Puzzle: ' + str(points))
    points = p2.parse_input_2(puzzle_input)
    print('2.2 Puzzle: ' + str(points))


if __name__ == '__main__':
    main()
