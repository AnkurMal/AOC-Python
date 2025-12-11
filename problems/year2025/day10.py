from z3 import *

def solve_joltage(buttons, targets):
    opt = Optimize()
    button_vars = [Int(f'b{i}') for i in range(len(buttons))]
    
    for var in button_vars:
        opt.add(var >= 0)
    
    for counter_idx in range(len(targets)):
        affecting = [button_vars[i] for i, btn in enumerate(buttons) if counter_idx in btn]
        if affecting:
            opt.add(Sum(affecting) == targets[counter_idx])
        elif targets[counter_idx] != 0:
            return None
    
    opt.minimize(Sum(button_vars))
    return opt.model().eval(Sum(button_vars)).as_long() if opt.check() == sat else None

def parse_line(line):
    parts = line.split()
    buttons = [[int(x) for x in p[1:-1].split(',')] for p in parts[1:-1]]
    targets = [int(x) for x in parts[-1][1:-1].split(',')]
    return buttons, targets

def part_2():
    with open('data/year2025/day10.txt', 'r') as f:
        data = f.read()
        total = 0
        for line in data.strip().split('\n'):
            buttons, targets = parse_line(line)
            result = solve_joltage(buttons, targets)
            if result:
                total += result

    print("Part 2:", total)