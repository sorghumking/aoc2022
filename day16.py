import re
from dataclasses import dataclass

@dataclass
class Node:
    valve: str
    flow_rate: int
    tunnels: list
    valve_open: bool = False

    def is_open(self):
        return self.valve_open

    def open(self):
        self.valve_open = True


class RouteFinder:
    def __init__(self, nodes):
        self.nodes = nodes
        self.best_route = None

    def find_best_route(self, loc: Node, dest: Node):
        self.best_route = None
        route = []
        self._find_best_route(loc, dest, route)
        return self.best_route[1:] # omit loc

    def _find_best_route(self, loc: Node, dest: Node, route: list):
        route.append(loc.valve)
        next_nodes = []
        for t in loc.tunnels:
            if t in route: # should never need to backtrack
                continue
            if t == dest.valve:
                route.append(dest.valve)
                if not self.best_route or len(route) < len(self.best_route):
                    self.best_route = route.copy()
                route.pop()
                continue
            next_nodes.append(nodes[t])
        for nn in next_nodes:
            self._find_best_route(self.nodes[nn.valve], dest, route)
        route.pop()


def best_routes(nodes, start_node):
    bests = {}
    good_nodes = [n for n in nodes.values() if n.flow_rate > 0] + [start_node]
    for lidx, loc in enumerate(good_nodes):
        for didx, dest in enumerate(good_nodes):
            if lidx == didx:
                continue
            shortest_route = RouteFinder(nodes).find_best_route(loc, dest)
            # print(f"Best route between {loc.valve} and {dest.valve} is {shortest_route}")
            if loc.valve not in bests:
                bests[loc.valve] = { dest.valve: shortest_route }
            else:
                bests[loc.valve][dest.valve] = shortest_route
    return bests

def next_node(loc, time, nodes_to_visit, bests):
    max_score = -1
    route = None
    for n in nodes_to_visit:
        if loc == n.valve:
            continue
        dist = len(bests[loc][n.valve])
        score = (time - dist - 1) * n.flow_rate
        # print(f"{n.valve} score: {time} - {dist} - 1 * {n.flow_rate} = {score}")
        if score > max_score:
            max_score = score
            route = bests[loc][n.valve]
    return route

@dataclass
class FlowTracker:
    flow_rate: int = 0
    pressure_released: int = 0

    def update(self):
        self.pressure_released += self.flow_rate

    def increase_rate(self, rate):
        self.flow_rate += rate


# def part1(nodes):
#     bests = best_routes(nodes, nodes['AA'])
#     tracker = FlowTracker()
#     loc = 'AA'
#     time = 30
#     poop = False
#     while time > 0:
#         print(f"Minute {30-time+1}: flow rate = {tracker.flow_rate}, {tracker.pressure_released} released.")
#         if not poop:
#             nodes_to_visit = [n for n in nodes.values() if n.flow_rate > 0 and not n.valve_open]
#         else:
#             nodes_to_visit = []
#         if len(nodes_to_visit) == 0:
#             time -= 1
#             tracker.update()
#             continue
#         dest_route = next_node(loc, time, nodes_to_visit, bests)
#         print(f"Next destination: {dest_route[-1]}")
#         for step in dest_route:
#             print(f"Minute {30-time+1}: moving to {step}")
#             loc = step
#             time -= 1
#             tracker.update()
#             if time == 0:
#                 break
#             if nodes[step] in nodes_to_visit:
#                 if not nodes[step].valve_open:
#                     print(f"Minute {30-time+1}: opening valve {step} with flow rate = {nodes[step].flow_rate}")
#                     nodes[step].open()
#                     time -= 1
#                     if time > 0:
#                         tracker.update()
#                         tracker.increase_rate(nodes[step].flow_rate)
#                         # poop = True
#             if time == 0:
#                 break
#     print(f"Total pressure released: {tracker.pressure_released}")

def part1(nodes):
    bests = best_routes(nodes, nodes['AA'])
    tracker = FlowTracker()    
    loc = 'AA'
    time = 30
    nodes_to_visit = [nodes['DD'], nodes['BB'], nodes['JJ'], nodes['HH'], nodes['EE'], nodes['CC']]
    route = bests['AA']['DD']
    while time > 0:
        tracker.update()
        print(f"Start of minute {30 - time + 1}, rate {tracker.flow_rate}, pressure released: {tracker.pressure_released}")
        if len(route) == 0: # reached destination, open valve if possible
            if not nodes[loc].valve_open:
                nodes[loc].open()
                print(f"Opening {loc} with rate {nodes[loc].flow_rate}")
                tracker.increase_rate(nodes[loc].flow_rate)
                nodes_to_visit.pop(nodes_to_visit.index(nodes[loc]))
            if len(nodes_to_visit) > 0: # find next route
                route = bests[loc][nodes_to_visit[0].valve]
                # route = next_node(loc, time, nodes_to_visit, bests) # my dumb next node method
        else: # move to next node
            loc = route[0]
            route.pop(0)
        time -= 1

def parse_input():
    nodes = {}
    with open('inputs/day16ex.txt') as f:
        for line in f.readlines():
            line = line.strip()
            valve_and_tunnels = re.findall(r'[A-Z][A-Z]', line)
            flow_rate = int(re.findall(r'[0-9]+', line)[0])
            valve = valve_and_tunnels[0]
            n = Node(valve, flow_rate, tunnels=valve_and_tunnels[1:])
            nodes[valve] = n
    return nodes



if __name__ == "__main__":
    nodes = parse_input()
    part1(nodes)
    # foobar(nodes)
    # for key, n in nodes.items():
        # print(f"Valve {key}, flow rate {n.flow_rate}, tunnels {n.tunnels}")