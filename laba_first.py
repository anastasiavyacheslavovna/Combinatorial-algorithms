from queue import Queue


def bfs(start_point, end_point, table, row, column):
    transitions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = Queue()
    queue.put(start_point)
    visited = {start_point}
    way = {start_point: None}

    while not queue.empty():
        point_x, point_y = queue.get()

        if (point_x, point_y) == (end_point[0], end_point[1]):
            path = []
            while (point_x, point_y) != start_point:
                path.append((point_x + 1, point_y + 1))
                point_x, point_y = way[(point_x, point_y)]
            path.append((start_point[0] + 1, start_point[1] + 1))
            return 'Y\n' + '\n'.join(f'{x} {y}' for x, y in reversed(path))

        for x, y in transitions:
            new_point_x, new_point_y = (point_x + x, point_y + y)
            if (((0, 0) <= (new_point_x, new_point_y) <= (row, column)) and
                    ((new_point_x, new_point_y) not in visited) and
                    (table[new_point_x][new_point_y] == 0)):
                visited.add((new_point_x, new_point_y))
                queue.put((new_point_x, new_point_y))
                way[(new_point_x, new_point_y)] = (point_x, point_y)

    return 'N'


if __name__ == '__main__':
    with open('in.txt', 'r') as file:
        count_row = int(file.readline().strip())
        count_column = int(file.readline().strip())
        matrix = [[int(j) for j in file.readline().split()] for i in range(count_row)]
        x_point_start, y_point_start = map(int, file.readline().split())
        x_point_end, y_point_end = map(int, file.readline().split())

    result = bfs((x_point_start - 1, y_point_start - 1), (x_point_end - 1,
                 y_point_end - 1), matrix, count_row, count_column)

    with open('out.txt', 'w') as file:
        file.write(result)
