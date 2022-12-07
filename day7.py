from dataclasses import dataclass

@dataclass
class Dir:
    name: str
    files: list
    dirs: list
    parent: any

    def get_dir(self, dirname):
        for d in self.dirs:
            if d.name == dirname:
                return d

    def __repr__(self):
        return self.name

def part1(cmds):
    root_dir = Dir('/', [], [], None)
    cur_dir = root_dir
    for cmd, arg in cmds:
        if cmd == 'cd':
            if arg == '..':
                cur_dir = cur_dir.parent
            elif arg == '/':
                cur_dir = root_dir
            else:
                cur_dir = cur_dir.get_dir(arg)
        elif cmd == 'ls':
            cur_dir.files = [(f.split()[1], int(f.split()[0])) for f in arg if f[0].isdigit()]
            cur_dir.dirs = [Dir(f.split()[1], [], [], cur_dir) for f in arg if f.startswith('dir')]

    sizes = []
    root_size = get_size(root_dir, sizes)
    sizes.append(('/', root_size))
    print(sizes)

    print(f"Total of dirs < 100000: {sum([s[1] for s in sizes if s[1] <= 100000])}")

def get_size(dir, sizes):
    sz = 0
    for f in dir.files:
        sz += f[1]
    for subdir in dir.dirs:
        sz += get_size(subdir, sizes)
    sizes.append((dir.name, sz))
    return sz



def print_dir(dir, level):
    print(f"{'  '*level}{dir.name} (dir)")
    for d in dir.dirs:
        print_dir(d, level+1)
    for f in dir.files:
        print(f"{'  '*(level+1)}{f}")


def parse_input(file):
    cmds = []
    with open(file) as f:
        lines = [l.strip() for l in f.readlines()]
        ls_lines = []
        for line_idx, line in enumerate(lines):
            if line.startswith('$') and len(ls_lines) > 0:
                cmds.append(('ls', ls_lines))
                ls_lines = []
            if line.startswith('$ cd'):
                cmds.append(('cd', line[5:]))
            elif not line.startswith('$'): # ls output
                ls_lines.append(line)
                if line_idx == len(lines)-1:
                    cmds.append(('ls', ls_lines))

    return cmds

if __name__ == "__main__":
    cmds = parse_input('inputs/day7.txt')
    # print(cmds)
    part1(cmds)