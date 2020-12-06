from graph import Graph
import sys
import getopt

def usage():
    print("Usage: python3 main.py \n\t-w <write results to file: no argument>\n\t-g <generate random graph with N vertices: int>")

if __name__ == "__main__":
    # initialization of random variables
    num_vertices = None
    write_flag = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hwg:", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for o, a in opts:
        
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o == "-w":
            write_flag = True
        elif o == "-g":
            try:
                num_vertices = int(a)
                assert int(a)>1, "chunksize bigger than 1"
            except:
                usage()
                sys.exit()

    # Call in random graph generator
    if num_vertices != None:
        pass
    # Test the scenarios we know are working
    else:
        # Graph Creation and definition, by adding edges
        # Test nº 1
        """
        graph = Graph(4)
        graph.add_edge(0,1)
        graph.add_edge(0,2)
        graph.add_edge(1,2)
        graph.add_edge(2,3)

        result = graph.color_matrix()
        print("Chromatic Index calculated correctly? %s" % (3==result))


        # Test nº 2
        graph = Graph(5)
        graph.add_edge(0,1)
        graph.add_edge(0,2)
        graph.add_edge(0,3)
        graph.add_edge(0,4)

        graph.add_edge(1,2)
        graph.add_edge(1,4)

        graph.add_edge(2,3)

        graph.add_edge(0,2)

        result = graph.color_matrix()
        print("Chromatic Index calculated correctly? %s" % (5==result))
        """
        # Test nº 3
        graph = Graph(3)
        graph.add_edge(0,1)
        graph.add_edge(0,2)
        graph.add_edge(1,2)

        result = graph.color_matrix()
        print("Chromatic Index calculated correctly? %s" % (3==result))

        # Available functions for visualizing matrixes
        graph.print_adj_matrix()    
        graph.print_colors_matrix()   
