# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 5000
# ports for the nodes connected to this node
connected_nodes = [5010, 5020, 5050]

node = GossipNode(port, connected_nodes)