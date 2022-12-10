def part1(trees):
    wid = len(trees[0])
    hit = len(trees)
    visible_count = 0
    for row in range(1,wid-1):
        for col in range(1,hit-1):
            if is_visible(trees, row, col):
                visible_count += 1
    visible_count += wid*2 + (hit-2)*2
    print(f"Visible tree count: {visible_count}")

def is_visible(trees, r, c):
    test_tree = trees[r][c]
    if max(right(trees, r, c)) < test_tree or max(left(trees, r, c)) < test_tree or \
        max(up(trees, r, c)) < test_tree or max(down(trees, r, c)) < test_tree:
        return True
    return False

def right(trees, r, c):
    return trees[r][c+1:]

def left(trees, r, c):
    return list(reversed(trees[r][:c])) # reverse for part2 view calc

def up(trees, r, c):
    return list(reversed([trees[row][c] for row in range(r)])) # reverse for part2 view calc

def down(trees, r, c):
    return [trees[row][c] for row in range(r+1, len(trees))]

def part2(trees):
    wid = len(trees[0])
    hit = len(trees)
    max_scenic = 0
    # edge trees will have score 0 and can be ignored
    for row in range(1,wid-1):
        for col in range(1,hit-1):
            scenic_score = calc_score(trees, row, col)
            if scenic_score > max_scenic:
                max_scenic = scenic_score
    print(f"Max scenic score: {max_scenic}")

def calc_score(trees, row, col):
    test_tree = trees[row][col]
    r = right(trees, row, col)
    l = left(trees, row, col)
    u = up(trees, row, col)
    d = down(trees, row, col)
    score = 1
    for view in [r, l, u, d]:
        view_dist = 0
        for tree in view:
            view_dist += 1
            if tree >= test_tree:
                break
        score *= view_dist
    return score

def parse_input():
    trees = []
    with open('inputs/day8.txt') as f:
        for line in f.readlines():
            trees.append([int(tree) for tree in line.strip()])
    return trees

if __name__ == "__main__":
    trees = parse_input()
    part1(trees)
    part2(trees)