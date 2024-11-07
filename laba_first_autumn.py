def distance(point_first, point_second):
    x_first, y_first = map(int, point_first.split())
    x_second, y_second = map(int, point_second.split())

    dist = abs(x_first - x_second) + abs(y_second - y_first)
    return dist


def kraskal(vert, edge):
    vertex = {int(i) for i in range(vert)}
    visited = set()
    wt = 0
    way = [[] for i in range(vert)]

    ind = 0
    first_vert = edge[0][0]
    second_vert = edge[0][1]
    way[first_vert].append(second_vert)
    way[second_vert].append(first_vert)
    wt += edge[0][2]
    visited.add(first_vert)
    vertex.discard(first_vert)
    visited.add(second_vert)
    vertex.discard(second_vert)

    while bool(vertex):
        for i in edge:
            new_vert_f = i[0]
            new_vert_s = i[1]

            if (new_vert_f in visited and new_vert_s in vertex):
                wt += i[2]
                visited.add(new_vert_s)
                vertex.discard(new_vert_s)
                way[new_vert_f].append(new_vert_s)
                way[new_vert_s].append(new_vert_f)
                break
            elif (new_vert_s in visited and new_vert_f in vertex):
                wt += i[2]
                visited.add(new_vert_f)
                vertex.discard(new_vert_f)
                way[new_vert_f].append(new_vert_s)
                way[new_vert_s].append(new_vert_f)
                break

    way = [sorted(i) for i in way]
    ans = ""
    for i in range(vert):
        for j in way[i]:
            ans += str(j + 1) + ' '
        ans += '0' + '\n'
    ans += str(wt)

    return ans


if __name__ == '__main__':
    with open ("in.txt", "r") as file:
        count_vert = int(file.readline().strip())
        coordinates_vert = dict()
        for i in range (count_vert):
            coordinates_vert[i] = file.readline().strip()

    edge_mass = []
    n = 0

    for i in range(count_vert):
        for j in range(i + 1, count_vert):
            edge_mass.append([i, j, distance(coordinates_vert[i], coordinates_vert[j])])

    edge_mass.sort(key=lambda k: k[2])
    ans = kraskal(count_vert, edge_mass)

    with open ("out.txt", "w") as file:
        file.write(ans)
