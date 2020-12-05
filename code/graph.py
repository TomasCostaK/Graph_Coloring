import sys

class Graph:
    def __init__(self, num_vertices):
        # Initialize array and declare num_vertices
        self.num_vertices = num_vertices
        self.adjecency_matrix = [0] * num_vertices
        self.colors_matrix = [0] * num_vertices

        # maximum colors is always (num_vertices-1) factorial

        # Initialize matrix
        for i in range(0, num_vertices):
            self.adjecency_matrix[i] = [0] * num_vertices
            self.colors_matrix[i] = [0] * num_vertices

    def add_edge(self, e1 , e2):
        self.adjecency_matrix[e1][e2] = 1
        self.adjecency_matrix[e2][e1] = 1 # graphs are undirected

    def color_matrix(self):
        # we iterate every vertice by ascending order
        # this doesnt result in the least amount of colors possible, but this is NP-Complete
        # this way we only iterate the top side of the matrix
        for row_id in range(0,self.num_vertices):
            # used colors for each vertice
            used_colors = []
            for column_id in range(0,self.num_vertices):
                # diagonal values of matrix
                if row_id == column_id or self.adjecency_matrix[row_id][column_id] == 0:
                    continue

                curr_value = self.colors_matrix[row_id][column_id]

                # first iteration and available values
                if curr_value == 0 and row_id == 0:
                    # we get the color 1 if there's no used color, otherwise we get color + 1, which is the next color
                    color = 1 if len(used_colors) == 0 else used_colors[-1]+1
                    # then we fill the matrix with the color
                    self.colors_matrix[row_id][column_id] = color
                    self.colors_matrix[column_id][row_id] = color
                    used_colors.append(color)

                elif curr_value == 0:
                    print("Going for: G[%d][%d]" % (row_id,column_id))
                    for i in range(0,row_id):
                        if self.adjecency_matrix[row_id][i] == 0:
                            continue
                        for j in range(0, len(self.adjecency_matrix[i])):
                            print("Analyzing: C[%d][%d] = %d" % (i,j, self.colors_matrix[i][j]))

                    color = 1 if len(used_colors) == 0 else used_colors[-1]+1
                    # then we fill the matrix with the color
                    self.colors_matrix[row_id][column_id] = color
                    self.colors_matrix[column_id][row_id] = color
                    used_colors.append(color)
                else:
                    pass
        
        print("Colors: ", self.colors_matrix)


    # Print matrix for debugging purposes
    def print_matrix(self):
        print("Adjacency: ",self.adjecency_matrix)