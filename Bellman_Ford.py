# making a dictionary out of parsed input data (faster than list, about O(1))
def make_graph_dict(data_list):
    key_value_pairs = list()
    for item in data_list:
        item = item[0:-1]
        parsed_symbols = [int(x) for x in item.split() if x]
        it = iter(parsed_symbols)
        key_value_pairs.append(list(zip(it, it)))
    graph = {i: dict(v) for i, v in enumerate(key_value_pairs, 1)}
    return graph


def bellman_ford_algorithm(graph, source):

    # step 1: distance and previous for each node
    dist, previous = dict(), dict()
    for node in graph:
        dist[node], previous[node] = float('inf'), None
    dist[source] = 0

    # step 2: relax the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                if dist[neighbour] > dist[node] + graph[node][neighbour]:
                    dist[neighbour], previous[neighbour] = dist[node] + graph[node][neighbour], node

    # step 3: check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            try:
                assert dist[neighbour] <= dist[node] + graph[node][neighbour], 'Negative cycle found!'
            except AssertionError as e:
                print(e)

    return dist, previous


# restores the path
def get_path_to_target(previous, target):
    cur = target
    path = []
    while cur is not None:
        path.append(cur)
        cur = previous[cur]
    return path


# output handler
def write_out_to_file(path: list):
    with open('out.txt', 'w') as out_file:
        if path is None:
            out_file.write('N')
        else:
            out_file.write('Y' + '\n')
            for vertex in path:
                out_file.write(str(vertex) + ' ')
            out_file.write('\n' + str(distance[start]))


if __name__ == '__main__':
    # input handler
    with open('in.txt', 'r') as file:
        data = [x.strip() for x in file.readlines()]
        num_vertices = int(data[0])
        start, target = int(data[-2]), int(data[-1])
    # print(data)                           # for debugging purposes
    # print(num_vertices)
    # print(start, target)
    graph = make_graph_dict(data[1:-2])
    previous, distance = bellman_ford_algorithm(graph, target)[1], bellman_ford_algorithm(graph, target)[0]
    resulting_path = get_path_to_target(previous, start)
    write_out_to_file(resulting_path)
