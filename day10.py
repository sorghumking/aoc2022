class CPU:
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

class CRT:
    lines = []
    cur_line = []
    sprite_pos = 1

    def draw(self, cycle):
        pix = (cycle-1) % 40
        if self.sprite_pos - 1 <= pix <= self.sprite_pos + 1:
            self.cur_line.append('#')
        else:
            self.cur_line.append('.')

    def move_sprite(self, new_pos):
        self.sprite_pos = new_pos

    def new_line(self):
        self.lines.append(self.cur_line)
        self.cur_line = []

    def render(self):
        for line in self.lines:
            print(''.join(line))


def part2(program):
    cpu = CPU()
    crt = CRT()
    for inst in program:
        if inst[0] == 'noop':
            cpu.noop()
        else:
            cpu.addx(inst[1])
        while True:
            if (cpu.cycle-1) % 40 == 0:
                crt.new_line()
            crt.draw(cpu.cycle)
            if cpu.ready():
                cpu.end()
                crt.move_sprite(cpu.X)
                break
            else:
                cpu.step()
    crt.new_line()
    crt.render()

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
    part2(program)