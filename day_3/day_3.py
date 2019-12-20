with open('input.txt', 'r') as f:
    lines = f.readlines()

    line_1 = lines[0].strip('\n').split(',')
    line_2 = lines[1].strip('\n').split(',')


def to_wire_path(line):
    path = []
    positions = (0,0)
    path.append(positions)
    for item in line:
        last_position = path[-1]
        if 'R' in item:
            previous_end = last_position[1]
            new_end = previous_end + int(item[1:])
            print('Going RIGHT from ' + str(previous_end) + ' to ' + str(new_end))
            positions = [(last_position[0], x) for x in range(previous_end, new_end+1)]
            print('New postion is: ', positions[-1])
        if 'L' in item:
            previous_end = last_position[1]
            new_end = previous_end - int(item[1:])
            print('Going LEFT from ' + str(previous_end) + ' to ' + str(new_end))
            positions = [(last_position[0], x) for x in range(new_end, previous_end + 1)]
            positions = list(reversed(positions))
            print('New postion is: ', positions[-1])
        if 'D' in item:
            previous_end = last_position[0]
            new_end = previous_end - int(item[1:])
            print('Going DOWN from ' + str(previous_end) + ' to ' + str(new_end))
            positions = [(x, last_position[1]) for x in range(new_end, previous_end + 1)]
            positions = list(reversed(positions))
            print('New postion is: ', positions[-1])
        if 'U' in item:
            previous_end = last_position[0]
            new_end = previous_end + int(item[1:])
            print('Going UP from ' + str(previous_end) + ' to ' + str(new_end))
            positions = [(x, last_position[1]) for x in range(previous_end, new_end + 1)]
            print('New postion is: ', positions[-1])
        coordinates = positions.copy()
        path.extend(coordinates)
    return path



wire1_path = to_wire_path(line_1)
wire2_path = to_wire_path(line_2)
from collections import OrderedDict
wire2_path = list(OrderedDict.fromkeys(wire2_path))
wire1_path = list(OrderedDict.fromkeys(wire1_path))
print('Wire 1 instructions: ', line_1)
print('Wire 1 coordinates: ', wire1_path)
print('Wire 2 instructions: ', line_2)
print('Wire 2 coordinates: ', wire2_path)
intersections = set(wire2_path).intersection(set(wire1_path))
intersections.discard((0,0))

def steps_to_intersection(wire_path):
    steps = {}
    for item in intersections:
        if item in wire_path:
            steps_to_intersection = wire_path.index(item)
            print('Index of '+ str(item)+  ' is '  + str(steps_to_intersection))
            steps[item] = steps_to_intersection
    return steps

steps_1 = steps_to_intersection(wire1_path)
steps_2 = steps_to_intersection(wire2_path)
combined_steps = {}
for key in steps_1.keys():
    combined_steps[key] = steps_1[key] + steps_2[key]

print(combined_steps)
distances = []
for (x,y) in intersections:
    distance = abs(x-0)+ abs(y-0)
    distances.append(distance)
print('Minimal distance is: ', min(distances))

print('Minimal number of steps is: ', min(combined_steps.items(), key=lambda x: x[1]) )