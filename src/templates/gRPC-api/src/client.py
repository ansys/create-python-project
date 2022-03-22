# Copyright (c) 2022, Ansys Inc. Unauthorised use, distribution or duplication is prohibited

from __future__ import print_function

import logging
import grpc
import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.join(Path(os.path.dirname(os.path.realpath(__file__))).parent, 'stubs'))

import pingserver_pb2
import pingserver_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pingserver_pb2_grpc.PingerStub(channel)
        response = stub.WhoPing(pingserver_pb2.UserRequest(name='you'))
    print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()

