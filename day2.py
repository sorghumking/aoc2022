def part1(rounds):
    move_dict = {'X':'A', 'Y':'B', 'Z':'C'}
    score_dict = {'A':1, 'B':2, 'C':3}
    total = 0
    for opp, me in rounds:
        me = move_dict[me]
        if opp == me:
            total += 3 + score_dict[me]
        elif ord(opp) - ord(me) in [1,-2]:
            total += score_dict[me]
        else:
            total += 6 + score_dict[me]
    print(f"Total: {total}")

def get_loser(opp):
    loser_dict = {'A':'C', 'B':'A', 'C':'B'}
    return loser_dict[opp]

def get_winner(opp):
    winner_dict = {'C':'A', 'A':'B', 'B':'C'}
    return winner_dict[opp]

def part2(rounds):
    # move_dict = {'X':'A', 'Y':'B', 'Z':'C'}
    score_dict = {'A':1, 'B':2, 'C':3}
    total = 0
    for opp, goal in rounds:
        if goal == 'X': # lose
            me = get_loser(opp)
            total += score_dict[me]
        elif goal == 'Y': # tie
            total += 3 + score_dict[opp]
        else: # win
            me = get_winner(opp)
            total += 6 + score_dict[me]
    print(f"Part 2 total: {total}")

def parse_input():
    rounds = []
    with open('inputs/day2.txt') as f:
        for l in f.readlines():
            line = l.strip()
            moves = l.split()
            rounds.append(moves)
    return rounds

if __name__ == "__main__":
    rounds = parse_input()
    # rounds = [['A','Y'],['B','X'],['C','Z']]
    part1(rounds)
    part2(rounds)