from math import floor
from copy import deepcopy
from dataclasses import dataclass

@dataclass
class Monkey:
    items: list[int]
    op: tuple
    test: int
    if_true: int
    if_false: int
    inspect_count: int = 0

    def do_op(self, worry):
        if self.op[1] == 'old':
            worry = worry * worry if self.op[0] == '*' else worry * 2
        else:
            worry = worry * self.op[1] if self.op[0] == '*' else worry + self.op[1]
        return worry
        

def part1(monkeys):
    for round in range(20):
        do_monkey_biz(monkeys, lambda w: floor(w/3))

    monkeys.sort(key=lambda m:m.inspect_count, reverse=True)
    print(f"Part 1 monkey business: {monkeys[0].inspect_count * monkeys[1].inspect_count}")

def part2(monkeys):
    lcm = 1
    for m in monkeys:
        lcm *= m.test

    for round in range(10000):
        do_monkey_biz(monkeys, lambda w: w % lcm)

    for idx, m in enumerate(monkeys):
        print(f"Monkey {idx}: {m.inspect_count} inspections.")

    monkeys.sort(key=lambda m:m.inspect_count, reverse=True)
    print(f"Part 2 monkey business: {monkeys[0].inspect_count * monkeys[1].inspect_count}")

def do_monkey_biz(monkeys, reduce_worry):
    for m in monkeys:
        for item_worry in m.items:
            item_worry = m.do_op(item_worry)
            item_worry = reduce_worry(item_worry)
            if item_worry % m.test == 0:
                monkeys[m.if_true].items.append(item_worry)
            else:
                monkeys[m.if_false].items.append(item_worry)
            m.inspect_count += 1
        m.items = []

def parse_input():
    monkeys = []
    with open('inputs/day11.txt') as f:
        lines = f.readlines()
        for idx in range(len(lines) // 7):
            monkey_lines = lines[idx*7:(idx+1)*7]
            monkeys.append(parse_monkey(monkey_lines))
    return monkeys

def parse_monkey(lines):
    items = [int(item) for item in lines[1].strip().replace('Starting items: ', '').split(',')]
    op_str = lines[2].replace('Operation: new = old ', '').strip()
    op = (op_str[0], op_str[2:] if op_str[2] == 'o' else int(op_str[2:]))
    test = int(lines[3].replace('Test: divisible by ', '').strip())
    if_true = int(lines[4].replace('If true: throw to monkey ', '').strip())
    if_false = int(lines[5].replace('If false: throw to monkey ', '').strip())
    return Monkey(items, op, test, if_true, if_false)


if __name__ == "__main__":
    monkeys = parse_input()
    part1(deepcopy(monkeys))
    part2(monkeys)