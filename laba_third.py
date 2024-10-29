def dijkstra(table, start, end, vertex):
    visited = dict()
    no_visited = {start:1}
    parent = dict()
    for i in range(1, vertex):
        no_visited[i] = 32767

    while no_visited.items():
        way, vert = min(zip(no_visited.values(), no_visited.keys()))
        visited[vert] = way
        del no_visited[vert]
        if (vert == end) and (way != 32767):
            ans = ''
            while vert != start:
                ans = ans + str(vert + 1)
                vert = parent[vert]
            ans = ans + str(start + 1)
            return 'Y\n' + ' '.join(ans[::-1]) + '\n' + str(way)
        for i in range(vertex):
            if i in no_visited:
                new_way = way * table[vert][i]
                if (table[vert][i] != 32767) and (new_way < no_visited[i]):
                    no_visited[i] = new_way
                    parent[i] = vert

    return 'N'

if __name__ == '__main__':
    with open('in.txt', 'r') as file:
        count_vertex = int(file.readline())
        matrix = [[int(j) for j in file.readline().split()]
                  for i in range(count_vertex)]
        start_vert = int(file.readline())
        end_vert = int(file.readline())

    result = dijkstra(matrix, start_vert - 1, end_vert - 1, count_vertex)

    with open('out.txt', 'w') as file:
        file.write(result)
