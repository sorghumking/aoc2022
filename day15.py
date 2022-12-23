import re

def man_dist(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def part1(sensors, test_y):
    # figure out min and max x
    xmin = min([s[0] - dist for s, _, dist in sensors])
    xmax = max([s[0] + dist for s, _, dist in sensors])
    print(f"searching y value {test_y} in x range {xmin}-{xmax}...")
    count = 0
    for x in range(xmin, xmax+1):
        test_coord = (x, test_y)
        in_range = False
        for s, b, dist in sensors:
            if test_coord == b:
                continue
            if man_dist(s, test_coord) <= dist:
                in_range = True
                break
        if in_range:
            count += 1
    print(f"Found {count} locations in range of a sensor.")

# return tuple (min, max) representing the sensor's x range
# at row y, clamped to mn and mx
def range_at_y(y, sensor, dist, mn, mx):
    if sensor[1] - dist <= y <= sensor[1] + dist:
        diff = dist - abs(sensor[1] - y)
        return (max(mn, sensor[0] - diff), min(mx, sensor[0] + diff))
    return None

# For each row, gather and merge the intervals for each sensor's x-range.
# If a row's intervals cannot be merged into a single row, the gap in
# those intervals is the distress beacon's location.
def part2(sensors, max_y):
    for y in range(max_y+1):
        if y % 100000 == 0:
            print(f"y = {y}")
        intervals = []
        for s, _, dist in sensors:
            interval = range_at_y(y, s, dist, 0, max_y)
            if interval is not None:
                # print(f"Sensor {s} dist {dist} has range {interval} at y = {y}")
                intervals.append(interval)
            # else:
                # print(f"Sensor {s} dist {dist} out of range at y = {y}")
        reduced = reduce(intervals)
        if len(reduced) > 1:
            print(f"Can't reduce {reduced} at y = {y}.")
            break

# Given list of intervals (min, max), merge as much as possible
# and return the resulting interval(s).
def reduce(intervals):
    last_len = -1
    while True:
        next_intervals = []
        cur = intervals[0]
        for next in intervals[1:]:
            merged = merge(cur, next)
            if merged is not None:
                cur = merged
            else:
                next_intervals.append(next)
        next_intervals.append(cur)
        intervals = next_intervals
        if len(intervals) == 1:
            break
        if len(intervals) == last_len:
            break
        last_len = len(intervals)
    return intervals

# int1 and int2 are intervals of form (min, max).
# If intervals overlap or are adjacent e.g. (1,2) and (3,4) merge to
# (1,4), return merged interval. Otherwise return None.
def merge(int1, int2):
    if int1[1] < int2[0]-1 or int1[0] > int2[1]+1:
        return None
    return (min(int1[0], int2[0]), max(int1[1], int2[1]))


def parse_input():
    sensors = []
    with open('inputs/day15.txt') as f:
        for line in f.readlines():
            line = line.strip()
            coords = [int(c) for c in re.findall(r'[\-0-9]+', line)]
            sensor = (coords[0], coords[1])
            beacon = (coords[2], coords[3])
            dist = man_dist(sensor, beacon)
            sensors.append((sensor, beacon, dist))
    return sensors

if __name__ == "__main__":
    sensors = parse_input()
    part1(sensors, 2000000)
    part2(sensors, 4000000)
