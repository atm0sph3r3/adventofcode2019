from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int


def get_points(instruction_set):
    current_x = 0
    current_y = 0
    points = dict()
    total_steps = 0

    for each in instruction_set:
        value = int(each[1:])

        for i in range(1, value + 1):
            total_steps += 1

            if each[0] == 'U':
                current_y += 1
            elif each[0] == 'D':
                current_y -= 1
            elif each[0] == 'L':
                current_x -= 1
            else:
                current_x += 1

            point = Point(current_x, current_y)
            if point not in points:
                points[point] = total_steps
    return points


with open('day3_input', 'r') as f:
    wire_1_points = get_points(f.readline().split(','))
    wire_2_points = get_points(f.readline().split(','))

    intersections = set(wire_1_points.keys()).intersection(set(wire_2_points.keys()))

    # part 1
    # print(min(intersections, key=lambda i: abs(i.x) + abs(i.y)))

    # part 2
    min_intersection = min(intersections, key=lambda i: wire_1_points[i] + wire_2_points[i])
    print(wire_1_points[min_intersection] + wire_2_points[min_intersection])


