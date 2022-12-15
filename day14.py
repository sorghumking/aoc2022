def set(rocks, coord):
    rocks[coord[1]][coord[0]] = 'o'

def at(rocks, coord):
    return rocks[coord[1]][coord[0]]

def get_next(coord):
    return [(coord[0], coord[1]+1), (coord[0]-1, coord[1]+1), (coord[0]+1, coord[1]+1)]

def move_sand(rocks, sand_pos):
    moved = False
    for next_pos in get_next(sand_pos):
        assert next_pos[0] >= 0, f"Invalid next x pos {next_pos[0]}"
        if at(rocks, next_pos) == '.':
            sand_pos = next_pos
            moved = True
            break
    if moved:
        if sand_pos[1] >= len(rocks) - 1:
            return False # into the abyss!
        return move_sand(rocks, sand_pos)
    set(rocks, sand_pos)
    return True # came to rest
        
def part2(rocks, min_x):
    count = 0
    while True:
        sand_pos = (500-min_x, 0)
        if at(rocks, sand_pos) == 'o':
            break
        came_to_rest = move_sand(rocks, sand_pos)
        assert came_to_rest
        if came_to_rest:
            count += 1
    # for row in rocks:
        # print(''.join(row))
    # print('-----------------------------')
    print(f"{count} grains of sand came to rest.")  

def part1(rocks, min_x):
    count = 0
    while True:
        sand_pos = (500-min_x, 0)
        came_to_rest = move_sand(rocks, sand_pos)
        if not came_to_rest:
            break
        else:
            count += 1
    # for row in rocks:
        # print(''.join(row))
    # print('-----------------------------')
    print(f"{count} grains of sand came to rest.")


def parse_input():
    rock_paths = []
    min_x = 10000
    max_x = -1
    min_y = 10000
    max_y = -1
    with open('inputs/day14.txt') as f:
        for line in f.readlines():
            line = line.strip()
            str_coords = line.split(" -> ")
            path = []
            for coords in str_coords:
                x, y = coords.split(",")
                x = int(x)
                y = int(y)
                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x
                if y < min_y:
                    min_y = y
                if y > max_y:
                    max_y = y
                path.append((x, y))
            rock_paths.append(path)
    # adjust min_x, max_x, max_y to ensure empty space for sand to
    # fall into abyss without IndexErrors
    min_x -= 1
    max_x += 1
    max_y += 1
    return rock_paths, min_x, max_x, min_y, max_y

# Return grid (list of lists) with rock positions, all x values
# offset by min_x such that min_x = 0. In hindsight using a
# dict keyed on (x,y) coords would be simpler.
def prep_rocks(rock_paths, min_x, max_x, max_y):
    rocks = []
    for y in range(max_y+1): # assume min_y is 0
        rocks.append(['.' for _ in range(max_x-min_x+1)])
    
    for path in rock_paths:
        idx = 0
        for end_x, end_y in path[1:]:
            start_x, start_y = path[idx]
            start_x -= min_x
            end_x -= min_x
            if start_x == end_x:
                assert start_y != end_y
                sy = min(start_y, end_y)
                ey = max(start_y, end_y)
                for y in range(sy, ey+1):
                    rocks[y][start_x] = '#'
            elif start_y == end_y:
                assert start_x != end_x
                sx = min(start_x, end_x)
                ex = max(start_x, end_x)
                for x in range(sx, ex+1):
                    rocks[start_y][x] = '#'
            idx += 1
    return rocks

# Return grid (list of lists) with rock positions, all x values
# offset by min_x such that min_x = 0. In hindsight using a
# dict keyed on (x,y) coords would be simpler.
def prep_rocks_with_floor(rock_paths, min_x, max_x, max_y):
    rocks = []
    for row, y in enumerate(range(max_y+1)): # assume min_y is 0
        if row == max_y:
            rocks.append(['#' for _ in range(max_x-min_x+1)])
        else:
            rocks.append(['.' for _ in range(max_x-min_x+1)])
    
    for path in rock_paths:
        idx = 0
        for end_x, end_y in path[1:]:
            start_x, start_y = path[idx]
            start_x -= min_x
            end_x -= min_x
            if start_x == end_x:
                assert start_y != end_y
                sy = min(start_y, end_y)
                ey = max(start_y, end_y)
                for y in range(sy, ey+1):
                    rocks[y][start_x] = '#'
            elif start_y == end_y:
                assert start_x != end_x
                sx = min(start_x, end_x)
                ex = max(start_x, end_x)
                for x in range(sx, ex+1):
                    rocks[start_y][x] = '#'
            idx += 1
    return rocks

if __name__ == "__main__":
    rock_paths, min_x, max_x, min_y, max_y = parse_input()
    rocks = prep_rocks(rock_paths, min_x, max_x, max_y)
    part1(rocks, min_x)

    min_x -= 150 # expand by fudge factor to allow all grains of sand to fall to floor
    max_x += 150
    max_y += 1 # floor is 2 units below max_y (already incremented by 1 in prep_rocks)
    rocks = prep_rocks_with_floor(rock_paths, min_x, max_x, max_y)
    part2(rocks, min_x)