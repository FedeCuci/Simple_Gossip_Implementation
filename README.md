<div align="center">

# Simple Gossip Implementation in Python

#### 🔧 Made with:
![](https://img.shields.io/badge/-Python-informational?style=flat&logo=Python&logoColor=white)

[Installation and Usage](#installation&usage)
•
[Limitations](#limitations) 
•
[Explanation](#installation)
•
[Node graph](#installation) 
•
[How it looks](#installation) 
•
[Motivation](#installation) 
•
[Demo](#installation) 

</div>

## Installation and Usage
All the libraries used in the scripts come from the Python standard library already, so there is no need to install external ones.

To test the scripts, place all files in the same directory and run all the Node_50xx.py scripts independently in a different terminal window or session. To visualize this better, you can use a tool like Tmux or something similar that allows you to split the same terminal session into different panes, as seen in the short video below. Note that the `Gossip.py` file does not need to be run; only the Node_50xx.py do.

You can try not to run certain nodes to observe how the nodes will react. If a node is not online and is not critical, the message is still going to be relayed to all nodes. You can also create new nodes and change the connections however you like!

## Limitations
This is obviously a very barebones implementation of the Gossip protocol and is missing many features in terms of privacy, security, robustness, etc. Below, I have listed some ways in which this implementation can be improved, but feel free to try whatever you like!

The nodes communicate with each other in a [connectionless](https://en.wikipedia.org/wiki/Connectionless_communication) way using the socket module. In very simple terms, it simply means that "the device at one end of the communication transmits data addressed to the other without first ensuring that the recipient is available and ready to receive the data."

## Explanation
The code in this script is fairly simple; however, because it is the implementation of a protocol, to understand the code you must first understand the basics of how the protocol works. To build this, the main articles that helped me were these:
  - [Gnutella: an Intro to Gossip](https://nakamoto.com/gnutella/)
  - [Bitcoin's P2P Network](https://nakamoto.com/bitcoins-p2p-network/)

## Node graph:

![Screenshot from 2023-01-21 22-10-19](https://user-images.githubusercontent.com/19730248/213887302-bb7fb3ba-741c-43f9-bf4a-727b711286bb.png)

## How it looks:

https://user-images.githubusercontent.com/19730248/213887484-e54b85b9-e849-4ab5-9684-22d4b05c4afd.mp4

## Motivation
The goal of this small project is to learn how multiple nodes in a network can communicate with each other in a decentralized way. The idea for the structure of this implementation comes from an old [Code Review Post](https://codereview.stackexchange.com/questions/95671/gossip-algorithm-in-distributed-systems/282643#282643) on Stack Exchange. The code in the post is broken, and this is a fixed implementation of it.

## Demo
If you'd like to learn more about how the script works, I have made a short [video](https://youtu.be/XR9BKhveduU) where I shortly run through the code. 

## Where to go from here & Further reading
There are many ways this script can be improved or optimized. Some ideas are:
  - Instead of hardcoding the connected nodes, try to let the nodes find each other organically. Hint take a look at [Boostrap nodes](https://nakamoto.com/bitcoins-p2p-network/#:~:text=protocol%20requires%20an-,bootstrap%20node,-to%20usher%20you). This might require more knowledge of networking.
  - Is there a way to check if a node is malicious? How can you trust any node to give you reliable and correct information?
  - How can you prevent a node from spamming the network? Hint: Take a look at how Bitcoin does it using a [Reputation system.](https://nakamoto.com/bitcoins-p2p-network/#:~:text=Bitcoin%20uses%20a-,reputation%20system,-to%20deal%20with)
  - What is ["Diffusion"](https://nakamoto.com/bitcoins-p2p-network/#:~:text=a%20method%20called-,diffusion,-.%20In%20diffusion%2C%20instead)? How does it increase privacy and would you be able to implement it in this script?
