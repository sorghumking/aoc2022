def part1(pairs):
    count = 0
    for p in pairs:
        if (p[0] <= p[2] and p[1] >= p[3]) or (p[2] <= p[0] and p[3] >= p[1]):
            count += 1
    print(f"Part 1 count: {count}")

def part2(pairs):
    count = 0
    for p in pairs:
        if p[0] <= p[3] and p[2] <= p[1]:
            count += 1
    print(f"Part 2 count: {count}")


def in_range(x, mn, mx):
    return mn <= x <= mx

def parse_input():
    with open('inputs/day4.txt') as f:
        pairs = []
        for line in f.readlines():
            pair = []
            l = line.strip()
            for p in l.split(','):
                pmin = int(p.split('-')[0])
                pmax = int(p.split('-')[1])
                pair.append(pmin)
                pair.append(pmax)
            pairs.append(pair)
        return pairs

if __name__ == "__main__":
    pairs = parse_input()
    ex = [
        [2,4,6,8],
        [2,3,4,5],
        [5,7,7,9],
        [2,8,3,7],
        [6,6,4,6],
        [2,6,4,8]
    ]
    part1(pairs)
    part2(pairs)