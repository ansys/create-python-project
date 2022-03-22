# Copyright (c) 2022, Ansys Inc. Unauthorised use, distribution or duplication is prohibited

from concurrent import futures
import logging
import grpc

import os
import sys
from pathlib import Path

import stubs.pingserver_pb2_grpc
from services.pinger import Pinger


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stubs.pingserver_pb2_grpc.add_PingerServicer_to_server(Pinger(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
