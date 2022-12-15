

def parse_input():
    rock_paths = []
    min_x = 10000
    max_x = -1
    min_y = 10000
    max_y = -1
    with open('inputs/day14ex.txt') as f:
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

if __name__ == "__main__":
    rock_paths, min_x, max_x, min_y, max_y = parse_input()
    rocks = prep_rocks(rock_paths, min_x, max_x, max_y)
    for row in rocks:
        print(''.join(row))