# Installation & Usage
All the libraries used in the scripts come in the Python standard library already, so no need to install external ones.

To test the scripts, place all files in the same directory and run all the scripts independently in a different terminal window/session. To visualize this better, you can use a tool like Tmux or similar, which allows you to split the same terminal session in different panes like seen in the GIF below. Note that the Gossip.py file does not need to be run, only the Node_50xx.py do.

You can try not to run certain nodes to observe how the nodes will react. If a node is not online, the other nodes will simply try to contact other nodes. If the node is not critical, then the message is going to be relayed to all nodes.

# Limitations
This is obviously a very barebones implementation of the Gossip protocol and is missing many features in terms of privacy, security, robustness etc. I have ideas on how to improve the implementation to make it more efficient, but that is still to come.

This script uses a "connectionless connection" using the socket module. That means that the nodes are not communicating through a network.

# Explanation
If you want to learn more about the Gossip protocol, this is where I got most of my information: https://nakamoto.com/gnutella/. 

# Node graph:

![Screenshot from 2023-01-21 22-10-19](https://user-images.githubusercontent.com/19730248/213887302-bb7fb3ba-741c-43f9-bf4a-727b711286bb.png)

# How it looks:

https://user-images.githubusercontent.com/19730248/213887484-e54b85b9-e849-4ab5-9684-22d4b05c4afd.mp4

# The goal
This is a simple implementation of the Gossip Protocol in Python. The goal of this small project is to learn how multiple nodes can communicate with each other in a decentralized way. The idea for the structure of this implementation comes from here: https://codereview.stackexchange.com/questions/95671/gossip-algorithm-in-distributed-systems/282643#282643.

# Video explanation
If you'd like to learn more about how the script works in video format, I have made a short video on it which I will have to re-record soon: https://youtu.be/XR9BKhveduU. 

# Where to go from here
There are many ways this script can be improved/optimized. Some ideas are:
  - Instead of hardcoding the connected nodes, try to let the nodes find each other organically.
  - Is there a way to check if a node is malicious? How can you trust any node to give you reliable and correct information?
  - How can you prevent a node from spamming the network?
  - How can you implement ["Diffusion"](https://nakamoto.com/bitcoins-p2p-network/#:~:text=a%20method%20called-,diffusion,-.%20In%20diffusion%2C%20instead) rather than the traditional propagation of messages?
