def accepts_nodes(fn):
	def wrapped(self, nodes = []):
		if isinstance(nodes, list):
			for node in nodes:
				if not isinstance(node, Node):
					raise TypeError("Not a node")
			fn(self, nodes)
		else:
			raise TypeError("Not a list of nodes")
		
	return wrapped

	
def accepts_node(fn):
	def wrapped(self, node):
		if isinstance(node, Node):
			fn(self, node)
		else:
			raise TypeError("Not a node")
	
	return wrapped

	
class Node(object):
	"""
	Node
	"""
	def __init__(self, node_id, connections):
		self.connections = set(connections)
		self.node_id = node_id
		self.dijkstra_reset()
		
	def dijkstra_reset(self):
		self.distance = None
		self.previous_node = None
		self.processed = False
		
	def edge_cost(self, next_node):
		connections = dict(self.connections)
		if next_node.node_id in connections:
			return connections[next_node.node_id]
		else:
			raise ValueError("{} is not a neighbour of {}".format(self, next_node))
		
	def __str__(self):
		return str(self.node_id)

			
class Graph(object):
	"""
	Graph
	"""
	def __init__(self, node_setup):
		"""
		node_setup is a list, with details for a single node as the item in the list.
		Each item should look like this:
		(node_id, [(node_connection1, distance1), (node_connection2, distance2), ...])
		"""
		self.nodes = self.set_up_nodes(node_setup)
		
	def set_up_nodes(self, node_setup):
		return {node_id: Node(node_id, connections) for (node_id, connections) in node_setup}		
		
		
class Path(object):
	"""
	Path
	"""
	@accepts_nodes
	def __init__(self, node_list = []):
		self.path = []
		for node in node_list:
			self.add(node)

	@accepts_node
	def add(self, node):
		self.path.append(node)
			
	@accepts_node
	def remove(self, node):
		self.path.remove(node)
		
	def __str__(self):
		return self.route_string()
		
	def route_string(self, separator = ", "):
		return separator.join(map(str, self.path))
		
	def edge_list(self):
		return zip(self.path[:-1], self.path[1:])
		
	def route_cost(self):
		return sum([node.edge_cost(next_node) for (node, next_node) in self.edge_list()])
