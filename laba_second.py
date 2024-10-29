def dfs(tabl):
    visited_first = {0}
    visited_second = set()
    stack = [0]

    while stack:
        vert = stack.pop()
        if vert in visited_first:
            for new_vert in tabl[vert]:
                if new_vert not in visited_first:
                    if new_vert not in visited_second:
                        visited_second.add(new_vert)
                        stack.append(new_vert)
                else:
                    return 'N'
        else:
            for new_vert in tabl[vert]:
                if new_vert not in visited_second:
                    if new_vert not in visited_first:
                        visited_first.add(new_vert)
                        stack.append(new_vert)
                else:
                    return 'N'
    ans = 'Y\n'
    for i in visited_first:
        ans = ans + str(i + 1) + ' '
    ans = ans[:-1] + '\n'
    for i in visited_second:
        ans = ans + str(i + 1) + ' '
    return ans[:-1]


if __name__ == '__main__':
    with open('in.txt', 'r') as file:
        count_vertex = int(file.readline().strip())
        graph = [[int(j) - 1 for j in file.readline().split()][:-1]
                 for i in range(count_vertex)]

    result = dfs(graph)

    with open('out.txt', 'w') as file:
        file.write(result)
