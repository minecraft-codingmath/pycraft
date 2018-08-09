"""
API handler module

"""

from threading import Thread
import queue
import zmq

class APIHandlerThread(Thread):
    """APIHandler class"""
    def __init__(self, msg_queue):
        """
        __init__ method

        Arguments:
        msg_queue -- the queue to put messages which feeds to Window
        """
        Thread.__init__(self)
        self.msg_queue = msg_queue

    def run(self):
        """
        run() method -- handles API requests

        More specifically, it reads api 'calls' from zmq and feed it to msg_queue.
        The api 'calls' are simply byte arrays encoded with utf-8, for now.
        It will be changed to msgpack-compressed json objects.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        # TODO: allow users to customize port
        socket.bind('tcp://*:1234')
        print('api handler thread started')

        while True:
            # TODO: use msgpack
            try:
                message = socket.recv()
            except zmq.error.ZMQError:
                # FIXME: doesn't seem to be right
                pass

            try:
                message_str = message.decode('utf-8')
            except UnicodeDecodeError:
                print('error: unicode decoding failed. skipping this api call.')
                continue

            self.msg_queue.put_nowait(message_str)
