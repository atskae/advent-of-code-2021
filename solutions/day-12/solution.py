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


def _r_find_paths(all_paths, cave_graph, visited, cave, path) -> list[str]:
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


def main(argv):
    cave_graph = parse_input_file(argv[1])
    for cave in cave_graph.keys():
        print(f"{cave} -> {cave_graph[cave]}")

    all_paths = set()
    for cave in cave_graph["start"]:
        _r_find_paths(all_paths, cave_graph, {}, cave, ["start"])

    for path in all_paths:
        print(path)

    print(f"Found {len(all_paths)} paths")


if __name__ == "__main__":
    main(sys.argv)
