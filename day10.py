class CPU():
    X = 1
    cycle = 0
    to_add = None
    req_cycles = 0

    def noop(self):
        self.step()

    def addx(self, amt):
        self.to_add = amt
        self.req_cycles = 2
        self.step()

    def ready(self):
        return self.req_cycles == 0

    def step(self):
        self.cycle += 1
        # print(f"Cycle {self.cycle}, X={self.X}")
        if self.req_cycles > 0:
            self.req_cycles -= 1

    def end(self):
        if self.req_cycles == 0 and self.to_add is not None:
            self.X += self.to_add
            # print(f"End of cycle {self.cycle}, adding {self.to_add} X={self.X}")
            self.to_add = None

def part1(program):
    strength = 0
    cpu = CPU()
    for inst in program:
        if inst[0] == 'noop':
            cpu.noop()
        else:
            cpu.addx(inst[1])
        while True:
            if cpu.cycle in [20, 60, 100, 140, 180, 220]:
                strength += cpu.X * cpu.cycle
                # print(f"During cycle {cpu.cycle} X={cpu.X}, strength={cpu.X*cpu.cycle}")
            if cpu.ready():
                cpu.end()
                break
            else:
                cpu.step()
    print(f"Signal strength: {strength}")


def parse_input():
    program = []
    with open('inputs/day10.txt') as f:
        for line in f.readlines():
            l = line.strip()
            if l == 'noop':
                program.append((l,))
            else:
                inst, amt = l.split(' ')
                program.append((inst, int(amt)))
    return program

if __name__ == "__main__":
    program = parse_input()
    part1(program)