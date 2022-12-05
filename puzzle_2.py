def get_game_points(option_1, option_2):
    if (option_1 == 'A' and option_2 == 'X') or (option_1 == 'B' and option_2 == 'Y') \
            or (option_1 == 'C' and option_2 == 'Z'):
        return 3
    if (option_1 == 'A' and option_2 == 'Y') or (option_1 == 'B' and option_2 == 'Z') \
            or (option_1 == 'C' and option_2 == 'X'):
        return 6
    return 0


def parse_input(puzzle_input):
    points = 0

    for index, i in enumerate(puzzle_input):
        puzzle_input[index] = puzzle_input[index].strip()
        option_a = puzzle_input[index][0]
        option_b = puzzle_input[index][2]

        match option_b:
            case 'X':
                points = points + 1
            case 'Y':
                points = points + 2
            case 'Z':
                points = points + 3

        points = points + get_game_points(option_a, option_b)

    return points


def parse_input_2(puzzle_input):
    points = 0

    for index, i in enumerate(puzzle_input):
        puzzle_input[index] = puzzle_input[index].strip()
        option_a = puzzle_input[index][0]
        option_b = puzzle_input[index][2]

        match option_b:
            case 'X':
                match option_a:
                    case 'A':
                        option_b = 'Z'
                    case 'B':
                        option_b = 'X'
                    case 'C':
                        option_b = 'Y'
            case 'Y':
                match option_a:
                    case 'A':
                        option_b = 'X'
                    case 'B':
                        option_b = 'Y'
                    case 'C':
                        option_b = 'Z'
            case 'Z':
                match option_a:
                    case 'A':
                        option_b = 'Y'
                    case 'B':
                        option_b = 'Z'
                    case 'C':
                        option_b = 'X'

        match option_b:
            case 'X':
                points = points + 1
            case 'Y':
                points = points + 2
            case 'Z':
                points = points + 3

        points = points + get_game_points(option_a, option_b)

    return points
