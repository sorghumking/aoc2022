def part1(cal_counts):
    max = -1
    for idx, cc in enumerate(cal_counts):
        if sum(cc) > max:
            max = sum(cc)
    print(f"Max calories: {max}")

def part2(cal_counts):
    cal_totals = [sum(cc) for cc in cal_counts]
    print(f"Total calories of top 3: {sum(sorted(cal_totals, reverse=True)[:3])}")

def parse_input():
    cal_counts = []
    with open('inputs/day1.txt') as f:
        cur_count = []
        for line in f.readlines():
            if line.strip() == "":
                cal_counts.append(cur_count)
                cur_count = []
            else:
                cur_count.append(int(line.strip()))
        cal_counts.append(cur_count) # last line
    return cal_counts

if __name__ == "__main__":
    cal_counts = parse_input()
    part1(cal_counts)
    part2(cal_counts)