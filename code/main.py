from graph import Graph

if __name__ == "__main__":

    # Graph Creation and definition, by adding edges
    graph = Graph(4)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,2)
    graph.add_edge(2,3)

    graph.color_matrix()

    graph.print_matrix()