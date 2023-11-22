# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 5030
# ports for the nodes connected to this node
connected_nodes = [5010]

node = GossipNode(port, connected_nodes)