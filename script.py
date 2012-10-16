from graph import Graph
from dijkstra import find_best_route

setup = [
(0, [(1,5), (2,4), (3,1), (4,1)]),
(1, [(0,5), (2,4), (3,2), (5,3)]),
(2, [(0,4), (1,4), (3,6), (5,3)]),
(3, [(0,1), (1,2), (2,6), (4,3)]),
(4, [(0,1), (3,3)]),
(5, [(1,3), (2,3)]),
]

mapping = {
	0:"Birmingham",
	1:"Luton",
	2:"London",
	3:"Leicester",
	4:"Walsall",
	5:"Harpenden",
}

def transform_connections(connections):
	return map(lambda t: (mapping[t[0]], t[1]), connections)
	
def transform_setup(setup):
	return map(lambda t: (mapping[t[0]], transform_connections(t[1])), setup)

uk = Graph(transform_setup(setup))

# find_best_route() returns a Path object
best_route = find_best_route(uk, "Walsall", "Harpenden")

print("Least distance from Walsall to Harpenden is:", best_route.route_cost())
print(best_route.route_string("->"))
