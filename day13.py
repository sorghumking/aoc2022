from functools import cmp_to_key

def get_datum(packet, idx):
    if idx >= len(packet):
        return None
    else:
        return packet[idx]

def prep_compare(left, right):
    if isinstance(left, int) and isinstance(right, list):
        return [left], right
    elif isinstance(left, list) and isinstance(right, int):
        return left, [right]
    return left, right

def compare(packet1, packet2):
    idx = 0
    while True:
        left = get_datum(packet1, idx)
        right = get_datum(packet2, idx)
        if left is None and right is None: # no resolution after completing both lists
            return 0
        if left is None: # left ran out, order is correct
            return -1
        if right is None: # right ran out, order is wrong
            return 1
        left, right = prep_compare(left, right)
        if isinstance(left, int) and isinstance(right, int):
            if left < right: 
                return -1
            elif right < left:
                return 1
        elif isinstance(left, list) and isinstance(right, list):
            result = compare(left, right)
            if result != 0:
                return result
        idx += 1

def part1(pairs):
    idx = 1
    correct_sum = 0
    for packet1, packet2 in pairs:
        correct = compare(packet1, packet2)
        if correct == -1:
            correct_sum += idx
        idx += 1
    print(f"Total of correct pair indices: {correct_sum}.")

def part2(pairs):
    packets = [[[2]], [[6]]]
    for p1, p2 in pairs:
        packets += [p1,p2]

    packets = sorted(packets, key=cmp_to_key(compare))
    div1 = packets.index([[2]]) + 1
    div2 = packets.index([[6]]) + 1
    print(f"Decoder key = {div1} * {div2} = {div1*div2}.")

def parse_input():
    pairs = []
    with open('inputs/day13.txt') as f:
        pair = []
        for idx, line in enumerate(f.readlines()):
            if idx % 3 in [0,1]:
                pair.append(eval(line.strip()))
            if idx % 3 == 1:
                pairs.append(pair)
                pair = []
    return pairs

if __name__ == "__main__":
    pairs = parse_input()
    part1(pairs)
    part2(pairs)