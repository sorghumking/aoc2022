
def find_marker(seq, seq_len, test):
    for idx in range(len(seq)-seq_len):
        quad = seq[idx:idx+seq_len]
        if test(quad):
            print(f"Found marker {quad}, count {idx+seq_len}")
            break

def part1(seq):
    find_marker(seq, 4, lambda quad:len(set(quad)) == 4)

def part2(seq):
    find_marker(seq, 14, lambda subseq:len(set(subseq)) == 14)


def parse_input():
    with open('inputs/day6.txt') as f:
        seq = f.readline().strip()
    return seq

if __name__ == "__main__":
    seq = parse_input()
    part1(seq)
    part2(seq)