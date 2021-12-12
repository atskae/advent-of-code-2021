import sys


def parse_input_file(input_file_name) -> dict[str, list[str]]:
    print(f"Reading input: {input_file_name}")

    # Mapping: cave -> list of adjacent caves
    cave_graph = {}
    with open(input_file_name, "r") as f:
        for line in f:
            edge = line.strip().split('-')
            c0 = edge[0]
            c1 = edge[1]
            if c0 not in cave_graph:
                cave_graph[c0] = []
            cave_graph[c0].append(c1)

            # Add the other direction into the graph
            if c1 not in cave_graph:
                cave_graph[c1] = []
            cave_graph[c1].append(c0)

    return cave_graph


def _r_find_paths(all_paths, cave_graph, visited, cave, path):
    if cave in visited and cave.islower():
        return
    if cave == "start":
        return
    if cave == "end":
        final_path = tuple(path[:] + [cave])
        all_paths.add(final_path)
        return

    visited[cave] = True
    current_path = path[:] + [cave]
    for adj_cave in cave_graph[cave]:
        _r_find_paths(all_paths, cave_graph, dict(visited), adj_cave, current_path[:])


def _r_find_new_paths(all_paths, cave_graph, visited, special_small_cave, cave, path):
    if cave in visited and cave.islower():
        if cave != special_small_cave:
            return
        else:
            if visited[cave] == 2:
                return
    if cave == "start":
        return
    if cave == "end":
        final_path = tuple(path[:] + [cave])
        all_paths.add(final_path)
        return

    if cave not in visited:
        visited[cave] = 0
    visited[cave] += 1

    current_path = path[:] + [cave]
    for adj_cave in cave_graph[cave]:
        _r_find_new_paths(all_paths, cave_graph, dict(visited), special_small_cave, adj_cave, current_path[:])


def main(argv):
    cave_graph = parse_input_file(argv[1])
    for cave in cave_graph.keys():
        print(f"{cave} -> {cave_graph[cave]}")

    # Part 1
    all_paths = set()
    for cave in cave_graph["start"]:
        _r_find_paths(all_paths, cave_graph, {}, cave, ["start"])

    for path in all_paths:
        print(path)

    print(f"Found {len(all_paths)} paths")

    # Part 2
    small_caves = []
    for cave in cave_graph.keys():
        if cave.islower() and (cave != "start" and cave != "end"):
            small_caves.append(cave)
    print(f"All small caves: {small_caves}")

    all_new_paths = set()
    # The special_small_cave can be visited at most twice
    for special_small_cave in small_caves:
        for cave in cave_graph["start"]:
            _r_find_new_paths(all_new_paths, cave_graph, {}, special_small_cave, cave, ["start"])

    for path in all_new_paths:
        print(path)

    print(f"Found {len(all_new_paths)} new paths")


if __name__ == "__main__":
    main(sys.argv)
