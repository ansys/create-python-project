from concurrent import futures
import logging
import grpc

import os
import sys
from pathlib import Path

import stubs.pingserver_pb2_grpc
from services.pinger import Pinger
from observability.logging import Logging


def serve():
    logger = Logging().logger
    port = 50051
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stubs.pingserver_pb2_grpc.add_PingerServicer_to_server(Pinger(), server)
    logger.info(f'Server starting and listening on {port}')
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
