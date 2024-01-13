import math
def readInputFile():
    filename = 'p083_matrix.txt'
    with open(filename, 'r') as file:
        lines = file.readlines()
        data_list = [line.strip().split(",") for line in lines]
        for i in range(len(data_list)):
            for j in range(len(data_list[i])):
                data_list[i][j] = int(data_list[i][j])
    return data_list

def getAdjacentPaths(current, L, graph, distance_graph):
    nodes = []
    if current[0]-1 >= 0:
        if distance_graph[current[0]][current[1]] + graph[current[0]-1][current[1]] < distance_graph[current[0]-1][current[1]]:
            nodes.append([current, [current[0]-1, current[1]]])
    if current[0]+1 < L:
        if distance_graph[current[0]][current[1]] + graph[current[0]+1][current[1]] < distance_graph[current[0]+1][current[1]]:
            nodes.append([current, [current[0]+1, current[1]]])
    if current[1]-1 >= 0:
        if distance_graph[current[0]][current[1]] + graph[current[0]][current[1]-1] < distance_graph[current[0]][current[1]-1]:
            nodes.append([current, [current[0], current[1]-1]])
    if current[1]+1 < L:
        if distance_graph[current[0]][current[1]] + graph[current[0]][current[1]+1] < distance_graph[current[0]][current[1]+1]:
            nodes.append([current, [current[0], current[1]+1]])
    return nodes


def main():
    graph = readInputFile()

    L = len(graph)
    distance_graph = [[math.inf for _ in range(L)] for _ in range(L)]
    start = [0,0]
    distance_graph[start[0]][start[1]] = graph[start[0]][start[1]]
    unvisited_paths = getAdjacentPaths(start, L, graph, distance_graph)
    while len(unvisited_paths) != 0:
        path = unvisited_paths.pop(0)
        if distance_graph[path[0][0]][path[0][1]] + graph[path[1][0]][path[1][1]] < distance_graph[path[1][0]][path[1][1]]:
            distance_graph[path[1][0]][path[1][1]] = distance_graph[path[0][0]][path[0][1]] + graph[path[1][0]][path[1][1]]
        new_paths = getAdjacentPaths([path[1][0], path[1][1]], L, graph, distance_graph)
        for i in new_paths:
            if i not in unvisited_paths:
                unvisited_paths.append(i)

    return distance_graph[L-1][L-1]


print(main())