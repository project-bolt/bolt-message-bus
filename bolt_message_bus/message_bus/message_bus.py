"""
Name: message_bux.py
Description: The message bus for bolt
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 08/12/2017
"""
import threading
from bolt_message_bus.message_bus import ConnectionHandler


class MessageBus(object):
    """The message server which acts as a message bus for bolt.

    The message bus acts as a common interconnect between the
    different components of the bolt ecosystem. The message bus
    utilizes the UDP type communication to handle the connected
    clients.
    """

    def __init__(self, host_address, host_port, debug=False):
        """Message bus initializer.

        Initializes the message bus based and setups all the infrastructure
        needed for running the message bus. Also initializes a failsafe
        mechanism for gracefully handling errors generated by the clients
        or the message bus threads.

        Debug Mode:
        Message Bus also implements a debug mode where all the actions being
        taken by the message bus are logged by the internal telemetry engine
        into a message bus debug file. The debug mode might come in handy for
        debugging in case the message bus starts to experience severe errors
        or is performing too slow.
        Since the debug mode profiles all the methods, running the message bus
        in debug mode in production could have significant costs associated
        with it and can also impact the performance.

        Keyword arguments:
        host_address -- Host address to run the message bus on
        host_port -- Host port where the message bus should bind to
        debug -- Should message bus run in debug mode (Default: False)
        """
        self.host_address = host_address
        self.host_port = host_port
        self.debug_mode = debug

        # Create a connection handler
        self.connection_handler = ConnectionHandler()
