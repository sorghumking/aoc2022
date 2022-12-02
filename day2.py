rps = ['A', 'B', 'C']
score_dict = {'A':1, 'B':2, 'C':3}

def part1(rounds):
    total = 0
    for opp, me in rounds:
        if opp == me:
            total += 3 + score_dict[me]
        elif ord(opp) - ord(me) in [1,-2]:
            total += score_dict[me]
        else:
            total += 6 + score_dict[me]
    print(f"Total: {total}")

def part2(rounds):
    total = 0
    for opp, goal in rounds:
        if goal == 'A': # lose
            me = rps[rps.index(opp) - 1]
            total += score_dict[me]
        elif goal == 'B': # tie
            total += 3 + score_dict[opp]
        else: # win
            me = rps[(rps.index(opp) + 1) % 3]
            total += 6 + score_dict[me]
    print(f"Part 2 total: {total}")

def parse_input():
    normalize_diff = ord('X') - ord('A')
    rounds = []
    with open('inputs/day2.txt') as f:
        for l in f.readlines():
            line = l.strip()
            opp, me = l.split()
            me = chr(ord(me) - normalize_diff)
            rounds.append([opp,me])
    return rounds

if __name__ == "__main__":
    rounds = parse_input()
    # rounds = [['A','Y'],['B','X'],['C','Z']]
    part1(rounds)
    part2(rounds)