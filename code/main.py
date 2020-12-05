from graph import Graph

if __name__ == "__main__":
    # Graph Creation and definition, by adding edges
    """
    # Test nº 3
    graph = Graph(4)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,2)
    graph.add_edge(2,3)

    # Test nº 2
    graph = Graph(3)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,2)

    # Test nº 2
    graph = Graph(3)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,2)
    """
    graph = Graph(5)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(0,3)
    graph.add_edge(0,4)

    graph.add_edge(1,2)
    graph.add_edge(1,4)

    graph.add_edge(2,3)

    graph.add_edge(0,2)


    # Function call and printing matrixes
    graph.color_matrix()
    graph.print_adj_matrix()    
    graph.print_colors_matrix()    