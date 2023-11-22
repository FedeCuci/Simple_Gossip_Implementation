import random
import socket
from threading import Thread
import time
from datetime import datetime
import hashlib


class GossipNode:
    # pass the port of the node and the ports of the nodes connected to it
    def __init__(self, port, connected_nodes):
        # create a new socket instance
        # use SOCK_DGRAM to be able to send data without a connection
        # being established (connectionless protocol)
        self.node = socket.socket(type=socket.SOCK_DGRAM)

        self.counter = 0

        # Store the previous message by any node
        self.time_transmitted = ''
        self.previous_message = ''
        self.received_messages = []

        # set the address, i.e(hostname and port) of the socket
        self.hostname = socket.gethostname()
        self.port = port

        # bind the address to the socket created
        self.node.bind((self.hostname, self.port))

        # set the ports of the nodes connected to it as susceptible nodes
        self.susceptible_nodes = connected_nodes

        # call the threads to begin the magic
        self.start_threads()

    def input_message(self):
        while True:
            # input message to send to all nodes
            if self.counter == 0:
                print('This is Node: [{}]\n'.format(self.port))
                self.counter += 1

            message_to_send = input("Enter a message to send: ")

            # call send message method and pass the input message.
            # encode the message into ascii
            self.transmit_message(message_to_send.encode('ascii'))

    def receive_message(self):
        while True:
            message_to_forward, address = self.node.recvfrom(1024)

            # Make sure not to keep sending the same message forever
            if self.previous_message == message_to_forward:
                continue
            self.previous_message = message_to_forward

            # Store the node who just sent this message
            previous_node = address[1]

            # sleep for 2 seconds in order to show difference in time
            time.sleep(1)

            # print message with the current time.
            # decode message so as to print it, as it was sent
            print("\nReceived message: '{0}'. From [{1}]"
                    .format(message_to_forward.decode('ascii')[19:], address[1]))
            
            print('\n\tNow forwarding to: {}\n'.format(self.susceptible_nodes))
            

            # call send message to forward the message to other susceptible(connected) nodes
            self.relay_message(message_to_forward, previous_node)

    def transmit_message(self, message):
        # Store time at which message is transmitted
        self.message_timestamp = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        message = self.message_timestamp + message.decode('ascii')
        self.previous_message = message.encode('ascii') # This has to be changed

        # Multicast message to connected nodes only
        for i in range(len(self.susceptible_nodes)):
            selected_port = self.susceptible_nodes[i]

            # since we are using connectionless protocol,
            # we will use 'sendto' to transmit the UDP message
            self.node.sendto(message.encode(), (self.hostname, selected_port))
            time.sleep(1)

    def relay_message(self, message, previous_node=0):
        # If you relay message, don't change timestamp
        for i in range(len(self.susceptible_nodes)):
            selected_port = self.susceptible_nodes[i]

            self.node.sendto(message, (self.hostname, selected_port))
            time.sleep(1)

    def start_threads(self):
        # two threads for entering and getting a message.
        # it will enable each node to be able to
        # enter a message and still be able to receive a message
        Thread(target=self.input_message).start()
        Thread(target=self.receive_message).start()