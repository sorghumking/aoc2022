from dataclasses import dataclass
import heapq

@dataclass
class Point:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __hash__(self):
        return tuple.__hash__((self.x, self.y))

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

@dataclass
class Grid:
    width: int
    height: int
    grid: list

    def get_height(self, pos: Point):
        return self.grid[pos.y][pos.x]

    def in_grid(self, pos: Point):
        return (0 <= pos.x < self.width) and (0 <= pos.y < self.height)


# I am too dumb to derive Dijkstra's Algorithm myself. Here is my slow
# impl from AoC 2021 Day 15.
def dijkstra(grid: Grid, start_pos: Point, end_pos: Point):
    verts = set()
    dists = {}
    prevs = {}

    for y in range(grid.height):
        for x in range(grid.width):
            dists[Point(x,y)] = float('inf') # infinity
            prevs[Point(x,y)] = None
            verts.add(Point(x,y))
    dists[start_pos] = 0
    
    while len(verts) > 0:
        if len(verts) % 1000 == 0:
            print(f"{len(verts)}, ", end='')
        v = min(verts, key=lambda v:dists[v]) # this is the bottleneck
        verts.remove(v)
        if v == end_pos:
            break
        for pt in possible_moves(grid, v):
            if pt in verts:
                new_dist = dists[v] + 1
                if new_dist < dists[pt]:
                    dists[pt] = new_dist
                    prevs[pt] = v
    return dists, prevs

# Adapated heapq implementation of Dijkstra from AoC 2021 Day 15 
def dijkstra_heapq(grid: Grid, start_pos: Point, end_pos: Point):
    verts = [(0, start_pos, [])]
    dists = {}
    for y in range(grid.height):
        for x in range(grid.width):
            dists[Point(x,y)] = float('inf') # infinity
    dists[start_pos] = 0
    seen = set()

    while True:
        try:
            dist, v, path = heapq.heappop(verts)
        except IndexError:
            # If we run out of verts before reaching the goal, it means
            # the goal is unreachable from the given point.
            return -1, None
        if v not in seen:
            seen.add(v)
            if v == end_pos:
                return dist, path + [v]
            for pt in possible_moves(grid, v):
                if dist + 1 < dists[pt]:
                    dists[pt] = dist + 1
                    heapq.heappush(verts, (dist + 1, pt, path + [v]))


def part1(grid: Grid, start: Point, goal: Point):
    risk, _ = dijkstra_heapq(grid, start, goal)
    print(f"Best distance to goal is {risk}")


def part2(grid: Grid, goal: Point):
    a_points = []
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get_height(Point(x,y)) == 'a':
                a_points.append(Point(x,y))
    
    min_dist = 10000
    for apt in a_points:
        dist, _ = dijkstra_heapq(grid, apt, goal)
        if dist == -1:
            print(f"No path from {apt}")
            continue
        if dist < min_dist:
            min_dist = dist
    print(f"Best distance from any a is {min_dist}")

def possible_moves(grid: Grid, pos: Point):
    moves = []
    cur_hit = grid.get_height(pos)
    for next_pos in [Point(pos.x+1,pos.y), Point(pos.x-1,pos.y), Point(pos.x,pos.y+1), Point(pos.x,pos.y-1)]:
        if not grid.in_grid(next_pos):
            continue
        if ord(grid.get_height(next_pos)) - 1 <= ord(cur_hit):
            moves.append(next_pos)
    return moves

def parse_input():
    with open('inputs/day12.txt') as f:
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
    part2(grid, end)