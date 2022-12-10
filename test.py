from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


class Knot:
    def __init__(self, point, prev=None) -> None:
        self.point = point
        self.prev = prev

    def move(self, direction, dist):
        next_x = self.point.x
        next_y = self.point.y

        if direction == 'R':
            next_x += dist
        elif direction == 'L':
            next_x -= dist
        elif direction == 'U':
            next_y += dist
        else:
            next_y -= dist

        self.point = Point(next_x, next_y)

    def adjacent(self, other):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = dx+self.point.x, dy+self.point.y
                if Point(nx, ny) == other.point:
                    return True

        return False

    def catchup(self, other):
        if other.point.y == self.point.y:
            direction = 'R' if other.point.x > self.point.x else 'L'
            self.move(direction, 1)
        elif other.point.x == self.point.x:
            direction = 'U' if other.point.y > self.point.y else 'D'
            self.move(direction, 1)
        else:
            direction = 'U' if other.point.y > self.point.y else 'D'
            self.move(direction, 1)
            direction = 'R' if other.point.x > self.point.x else 'L'
            self.move(direction, 1)


def solve_part_1(arr):
    seen = set([Point(0, 0)])
    tail = Knot(Point(0, 0))
    head = Knot(Point(0, 0))

    for direction, dist in arr:
        for _ in range(dist):
            head.move(direction, 1)
            if not head.adjacent(tail):
                tail.catchup(head)

            seen.add(tail.point)

    return len(seen)


def solve_part_2(arr):
    seen = set([Point(0, 0)])
    tail = Knot(Point(0, 0))
    head = Knot(Point(0, 0), prev=tail)
    curr = tail

    for _ in range(8):
        new_tail = Knot(Point(0, 0))
        curr.prev = new_tail
        curr = curr.prev

    for direction, dist in arr:
        for _ in range(dist):
            head.move(direction, 1)
            curr_head = head
            curr_tail = curr_head.prev

            while curr_tail:
                if not curr_head.adjacent(curr_tail):
                    curr_tail.catchup(curr_head)

                curr_head = curr_tail
                curr_tail = curr_tail.prev

            seen.add(curr_head.point)

    return len(seen)


if __name__ == '__main__':
    with open('input2.txt') as f:
        arr = []

        for line in f.readlines():
            direction, dist = line.strip().split()
            arr.append([direction, int(dist)])

        print(solve_part_1(arr))
        print(solve_part_2(arr))
