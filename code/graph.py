class Graph:
    def __init__(self, num_vertices):
        # Initialize array and declare num_vertices
        self.num_vertices = num_vertices
        self.adjecency_matrix = [0] * num_vertices

        # Initialize matrix
        for i in range(0, num_vertices):
            self.adjecency_matrix[i] = [0] * num_vertices

    def add_edge(self, e1 , e2):
        self.adjecency_matrix[e1][e2] = 1
        self.adjecency_matrix[e2][e1] = 1 # graphs are undirected
    # Print matrix for debugging purposes
    def print_matrix(self):
        print(self.adjecency_matrix)