
class Node(object):
	"""
	Node
	"""
	def __init__(self, node_id, connections):
		self.connections = set(connections)
		self.node_id = node_id
		self.reset()
	def reset(self):
		self.distance = None
		self.previous_node = None
		self.processed = False
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
		
		