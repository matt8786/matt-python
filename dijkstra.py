#
# Algorithm
#
	
def find_best_route(graph, start, end):
	"""
	Find the best route through the grid between the given start node and the given 
	end node.
	"""
	if start == end:
		best_route_found = True
	else:
		best_route_found = False
		graph.nodes[start].distance = 0
		reachable_unprocessed_nodes = set([graph.nodes[start]])
		
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
		closest_distance = None
		for node in reachable_unprocessed_nodes:
			if closest_distance is None or node.distance < closest_distance:
				closest_node = node
				closest_distance = node.distance
		
		assert closest_node.processed == False,                               \
		       "Processed node is in list of unprocessed nodes"
				
		if closest_node.node_id == end:
			best_route_found = True
		
		# Process this node
		if not best_route_found:
			reachable_unprocessed_nodes.remove(closest_node)
			closest_node.processed = True
			for (node_id, distance) in closest_node.connections:
				node = graph.nodes[node_id]
				if node.distance is None or closest_node.distance + distance < node.distance:
					node.distance = closest_node.distance + distance
					reachable_unprocessed_nodes.add(node)
					node.previous_node = closest_node
					
	if start is end:
		route = str(start) + "->" + str(end)
	else:
		route = str(end)
		current_node = graph.nodes[end]
		while current_node.previous_node is not None:
			route = str(current_node.previous_node) + "->" + route
			current_node = current_node.previous_node

	print("Least distance from", start, "to", end, "is:", graph.nodes[end].distance)
	print("Example route is:", route)
