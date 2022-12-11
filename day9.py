from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

dir_dict = {'R':1, 'L':-1, 'U':1, 'D':-1}

def part1(moves):
    head = Point(0,0)
    tail = Point(0,0)
    visited = [(0,0)]
    for dir, amt in moves:
        for step in range(amt):
            if dir in ['L', 'R']:
                head.x += dir_dict[dir]
            else:
                head.y += dir_dict[dir]
            if not adjacent(head, tail):
                dx, dy = get_deltas(head, tail)
                tail.x += dx
                tail.y += dy
                visited.append((tail.x, tail.y))
    print(f"Total points visited: {len(set(visited))}")

# assumes head and tail are not adjacent
def get_deltas(head, tail):
    dx = 0
    dy = 0
    if head.x != tail.x:
        dx = 1 if head.x > tail.x else -1
    if head.y != tail.y:
        dy = 1 if head.y > tail.y else -1
    return dx, dy


def part2(moves):
    head = Point(0,0)
    tail = Point(0,0)
    knots = [Point(0,0) for _ in range(8)]
    visited = set([(0,0)])
    for dir, amt in moves:
        for step in range(amt):
            if dir in ['L', 'R']:
                head.x += dir_dict[dir]
            else:
                head.y += dir_dict[dir]
            if not adjacent(head, tail):
                dx, dy = get_deltas(head, tail)
                tail.x += dx
                tail.y += dy
                prev_knot = tail
                for idx, k in enumerate(knots):
                    if not adjacent(prev_knot, k):
                        dx, dy = get_deltas(prev_knot, k)
                        k.x += dx
                        k.y += dy
                        prev_knot = k
                        if idx == len(knots) - 1:
                            visited.add((k.x, k.y))
                    else:
                        break
    print(f"Total points visited by tail: {len(visited)}")

def draw(head, tail, knots):
    for y in list(reversed(range(5))):
        for x in range(6):
            if head.x == x and head.y == y:
                print('H', end='')
            elif tail.x == x and tail.y == y:
                print('1', end='')
            else:
                blank = True
                for idx, k in enumerate(knots):
                    if k.x == x and k.y == y:
                        print(str(idx+2), end='')
                        blank = False
                        break
                if blank:
                    print('.', end='')
        print('\n')

def adjacent(head, tail):
    return abs(head.x - tail.x) <= 1 and abs(head.y - tail.y) <= 1

def parse_input():
    moves = []
    with open('inputs/day9.txt') as f:
        for line in f.readlines():
            dir, amt = line.strip().split(' ')
            moves.append((dir, int(amt)))
    return moves

if __name__ == "__main__":
    moves = parse_input()
    part1(moves)
    part2(moves)