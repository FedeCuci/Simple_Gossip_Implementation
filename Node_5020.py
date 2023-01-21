# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 5020
# ports for the nodes connected to this node
connected_nodes = [5000, 5050]

node = GossipNode(port, connected_nodes)