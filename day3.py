def part1(sacks):
    common_items = []
    for s in sacks:
        h1,h2 = s[:len(s)//2], s[len(s)//2:]
        for c in h1:
            if c in h2:
                common_items.append(c)
                break
    total_priority = sum([get_priority(ci) for ci in common_items])
    print(f"Total priority: {total_priority}")

def part2(sacks):
    assert int(len(sacks)/3) == len(sacks)//3
    badges = []
    for idx in range(len(sacks)//3):
        s1,s2,s3 = sacks[idx*3:(idx+1)*3]
        common = []
        for c in s1:
            if c in s2:
                common.append(c)
        for c in common:
            if c in s3:
                badges.append(c)
                break
    total_priority = sum([get_priority(b) for b in badges])
    print(f"Total badge priority: {total_priority}")


def get_priority(item):
    if item.isupper():
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1


def parse_input():
    sacks = []
    with open('inputs/day3.txt') as f:
        for line in f.readlines():
            l = line.strip()
            sacks.append(l)
    return sacks

if __name__ == "__main__":
    ex = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]
    sacks = parse_input()
    part1(sacks)
    part2(sacks)