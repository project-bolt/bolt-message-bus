"""
Name: connection_controller.py
Description: Connection handling mechanism for the message server
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 08/12/2017
"""


class ConnectionHandler(object):
    """Connection Handler to manage the client connectivity with the bus.

    ConnectionHandler acts as a central layer where all the clients register
    to and are kept track of. If there is no communication from the clients
    from a long time, the connection handler is responsible for ensuring that
    the resources associated with the connection are freed up and the
    connection is killed.
    """

    def __init__(self):
        """Client Connection Handler Initializer.

        Initializes the connection handler and prepares for the handling of
        new connections that are joining the message bus.
        """
        self.connection_topics = []
        self.connection_queue = {}
        self.valid_incoming = []

    def new_connection(self, topic, address):
        """Add a new connection.

        Keyword arguments:
        topic -- The topic to which a new connection should be grouped under
        address -- The address of the new connection

        Returns:
            Boolean
        """
        # We have a new type of client coming in, handle this behavior
        # gracefully
        if topic not in self.connection_topics:
            self.connection_topics.append(topic)
            self.connection_queue[topic] = []

        # We have the topic identified by now, let's move on to add our
        # connection object
        self.connection_queue[topic].append(address)
        self.valid_incoming.append(address)

    def get_connections(self, topic):
        """Return a list of connection addresses pertaining to the topic.

        Keyword arguments:
        topic -- The topic for which the connections should be searched

        Returns:
            List
        """
        if topic not in self.connection_topics:
            return []
        return self.connection_queue[topic]

    def get_topics(self):
        """Return a list of all the topics present.

        Returns:
            List
        """
        return self.connection_topics

    def remove_connection(self, address):
        """Remove the specified connection address from all the topics.

        Keyword arguments:
        address -- The address to be removed
        """
        topics = self.get_topics()
        for topic in topics:
            if address in self.connection_queue[topic]:
                self.connection_queue[topic].remove(address)
