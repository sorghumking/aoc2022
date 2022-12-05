def part1(stacks, moves):
    print(stacks)
    for amt, src, dst in moves:
        src -= 1 # input stack numbers are 1-based
        dst -= 1
        for _ in range(amt):
            crate = stacks[src].pop(0)
            stacks[dst].insert(0, crate)
    top_crates = ''.join([s[0] for s in stacks])
    print(f"Part 1: {top_crates}")

def part2(stacks, moves):
    print(stacks)
    for amt, src, dst in moves:
        src -= 1 # input stack numbers are 1-based
        dst -= 1
        crates = stacks[src][:amt]
        stacks[src] = stacks[src][amt:]
        stacks[dst] = crates + stacks[dst]
    top_crates = ''.join([s[0] for s in stacks])
    print(f"Part 2: {top_crates}")

def parse_input():
    stacks = [[] for i in range(9)]
    moves = []
    with open('inputs/day5.txt') as f:
        for line in f.readlines():
            if line[0] == '[':
                for count, c in enumerate(line.strip()):
                    if c == '[':
                        stacks[count // 4].append(line[count+1])
            elif line[0] == 'm':
                moves.append(parse_move_line(line.strip()))
    return stacks, moves

def parse_move_line(line):
    tokens = line.split()
    return [int(tokens[idx]) for idx in [1,3,5]]

from copy import deepcopy

if __name__ == "__main__":
    stacks, moves = parse_input()
    
    # deepcopy() stacks to ensure part2() isn't using
    # part1()-modified stacks! list.copy() is insufficient
    # because elements of stacks are lists themselves.
    part1(deepcopy(stacks), moves)
    part2(stacks, moves)