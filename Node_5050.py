# import the GossipNode class
from Gossip import GossipNode

# port for this node
port = 5050
# ports for the nodes connected to this node
connected_nodes = [5000, 5020]

node = GossipNode(port, connected_nodes)