from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __hash__(self):
        return tuple.__hash__((self.x, self.y))

@dataclass
class Grid:
    width: int
    height: int
    grid: list

    def get_height(self, pos: Point):
        return self.grid[pos.y][pos.x]

    def in_grid(self, pos: Point):
        return (0 <= pos.x < self.width) and (0 <= pos.y < self.height)



def part1(grid: Grid, start: Point, goal: Point):
    cur_pos = start
    path = [cur_pos]
    visited = set([cur_pos])
    moves = possible_moves(grid, cur_pos, path)
    for new_pos in moves:
        if do_move(grid, new_pos, goal, path, visited):
            print(f"Found path of length {len(path)} to goal!")
            print(path)
            break


def do_move(grid: Grid, pos: Point, goal: Point, path: list[Point], visited: set[Point]):
    path.append(pos)
    # visited.add(pos)
    # print(path)
    # print(f"cur: {pos}, path: {path}")
    if pos == goal:
        return True
    moves = possible_moves(grid, pos, path)
    # if len(moves) == 0:
        # visited.add(pos)
    for new_pos in moves:
        if new_pos in path or new_pos in visited:
            continue
        if do_move(grid, new_pos, goal, path, visited):
            return True
        else:
            path.pop()
            # visited.remove(new_pos)
    return False

def possible_moves(grid: Grid, pos: Point, path: list[Point]):
    moves = []
    cur_hit = grid.get_height(pos)
    for next_pos in [Point(pos.x+1,pos.y), Point(pos.x-1,pos.y), Point(pos.x,pos.y+1), Point(pos.x,pos.y-1)]:
        if not grid.in_grid(next_pos):
            # print(f"{next_pos} not in grid")
            continue
        elif next_pos in path:
            # print(f"{next_pos} already in path")
            continue
        # print(f"cur height: {cur_hit}, pos {next_pos} height: {grid.get_height(next_pos)}, ", end='')
        if ord(grid.get_height(next_pos)) - 1 <= ord(cur_hit):
            moves.append(next_pos)
    return moves

def parse_input():
    with open('inputs/day12ex.txt') as f:
        lines = [l.strip() for l in f.readlines()]
        grid = []
        for y, line in enumerate(lines):
            cur_line = []
            for x, c in enumerate(line):
                if c == 'S':
                    start = Point(x,len(lines)-1-y)
                    cur_line.append('a')
                elif c == 'E':
                    end = Point(x,len(lines)-1-y)
                    cur_line.append('z')
                else:
                    cur_line.append(c)
            grid.append(cur_line)
    return Grid(width=len(lines[0]), height=len(lines), grid=list(reversed(grid))), start, end

if __name__ == "__main__":
    grid, start, end = parse_input()
    part1(grid, start, end)