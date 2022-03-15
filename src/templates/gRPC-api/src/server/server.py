# Copyright (c) 2022, Ansys Inc. Unauthorised use, distribution or duplication is prohibited

from concurrent import futures
import logging
import grpc

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.join(Path(os.path.dirname(os.path.realpath(__file__))).parent, 'stubs'))

import pingserver_pb2
import pingserver_pb2_grpc

NumberPing = 0


class Pinger(pingserver_pb2_grpc.PingerServicer):

    def PingServer(self, request, context):
        global NumberPing
        NumberPing += 1
        return pingserver_pb2.PingReply(message=f'Hello, the server is healthy and it had been pinged {NumberPing} times!')

    def WhoPing(self, request, context):
        global NumberPing
        NumberPing += 1
        return pingserver_pb2.PingReply(message=f'Hello, the server is pinged by {request.name}!')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pingserver_pb2_grpc.add_PingerServicer_to_server(Pinger(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
