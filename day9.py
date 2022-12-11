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
                if dir in ['L', 'R']:
                    tail.x = head.x - dir_dict[dir]
                    tail.y = head.y
                else:
                    tail.y = head.y - dir_dict[dir]
                    tail.x = head.x
                visited.append((tail.x, tail.y))
    print(f"Total points visited: {len(set(visited))}")

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
                tail0 = Point(tail.x, tail.y)
                if dir in ['L', 'R']:
                    tail.x = head.x - dir_dict[dir]
                    tail.y = head.y
                else:
                    tail.y = head.y - dir_dict[dir]
                    tail.x = head.x
                dx = tail.x - tail0.x
                dy = tail.y - tail0.y

                knot_ahead = tail
                for idx, k in enumerate(knots):
                    if not adjacent(knot_ahead, k):
                        k.x += dx
                        k.y += dy
                        knot_ahead = k
                        if idx == len(knots)-1:
                            visited.add((k.x, k.y))
                    else:
                        break
            draw(head, tail, knots)
            print("-----------------------\n")
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
    with open('inputs/day9ex.txt') as f:
        for line in f.readlines():
            dir, amt = line.strip().split(' ')
            moves.append((dir, int(amt)))
    return moves

if __name__ == "__main__":
    moves = parse_input()
    # part1(moves)
    part2(moves)