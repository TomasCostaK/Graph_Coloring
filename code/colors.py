from constraintsearch import *

#Defining variables and values
variables = ['a','b','c','d','e']
values = ['r','g','b']

#Creating domains and edges
domains = { v:values for v in variables}
#Alterar estes edges para os proximos
edges = [ ('a','b') , ('b','c'), ('c','d') , ('d','a')] + [(v, 'e') for v in variables[:4]]
edges = [ (v2,v1) for (v1,v2) in edges ] + edges

graph = { e:(lambda v1,x1,v2,x2: x1!=x2) for e in edges }
colors = ConstraintSearch(domains,graph)

print(colors.search())

