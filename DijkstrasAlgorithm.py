class Node(object):
	def __init__(self):
		self.distance_from_start = -1
		self.previous_node = -1
		self.connections = set([])
		self.processed = False
	def add_connections(self, list):
		for (node, distance) in list:
			self.connections.add((node, distance))
				
setup = [
(0, [(1,5), (2,3), (3,1), (4,1)]),
(1, [(0,5), (2,4), (3,2), (5,3)]),
(2, [(0,3), (1,4), (3,6), (5, 3)]),
(3, [(0,1), (1,2), (2,6), (4,3)]),
(4, [(0,1), (3,3)]),
(5, [(1,3), (2,3)]),
]

def set_up_nodes(node_setup):
	node_list = []
	for (node, connections) in node_setup:
		node_list.append(Node())
		node_list[node].add_connections(connections)
	return node_list

#
# Algorithm
#
	
def find_best_route(start, end):
# Find the best route through the grid between the given start node and the given 
# end node
	if start is end:
		best_route_found = True
	else:
		best_route_found = False
		nodes = set_up_nodes(setup)
		nodes[start].distance_from_start = 0
		reachable_unprocessed_nodes = set([start])
		
	while not best_route_found:
		# 1. loop over the reachable but unprocessed nodes. Find the one with the 
		#    least distance from the start (X).
		# 2. For each node Y connected to X, take d(start,X) + d(X,Y) and see if it 
		#    is less than d(start, Y). If so, update node Y with a new distance and 
		#    a new previous node (X).
		# 3. If the end has been reached, iterate over all items in the reachable
		#    but unprocessed nodes. If d(start,end) <= d(start,node) for all of these
		#    nodes, then we have found the best route.

		# Find the unprocessed node closest to the start
		closest_distance = -1
		for node in reachable_unprocessed_nodes:
			if closest_distance < 0 or nodes[node].distance_from_start < closest_distance:
				closest_node = node
				closest_distance = nodes[node].distance_from_start
		
		assert nodes[closest_node].processed == False, "Processed node is in list of unprocessed nodes"
				
		if closest_node is end:
			best_route_found = True
		
		# Process this node
		if not best_route_found:
			reachable_unprocessed_nodes.remove(closest_node)
			nodes[closest_node].processed = True
			for (node, distance) in nodes[closest_node].connections:
				if nodes[node].distance_from_start < 0 or nodes[closest_node].distance_from_start + distance < nodes[node].distance_from_start:
					nodes[node].distance_from_start = nodes[closest_node].distance_from_start + distance
					reachable_unprocessed_nodes.add(node)
					nodes[node].previous_node = closest_node
					
	if start is end:
		route = str(start) + str(end)
	else:
		route = str(end)
		current_node = end
		while nodes[current_node].previous_node is not -1:
			route = str(nodes[current_node].previous_node) + route
			current_node = nodes[current_node].previous_node

	print("Least distance from", start, "to", end, "is:", nodes[end].distance_from_start)
	print("Example route is:", route)
	
#
# Testing
#
find_best_route(4,5)
