# Copyright (c) 2022, Ansys Inc. Unauthorised use, distribution or duplication is prohibited
from src.stubs.pingserver_pb2 import UserRequest, EmptyRequest


class TestServer:
    def test_first_ping(self, grpc_stub):
        request = EmptyRequest()
        response = grpc_stub.PingServer(request)
        assert response.message == 'Hello, the server is healthy and it had been pinged 1 times!'

    def test_who_ping(self, grpc_stub):
        request = UserRequest(name='you')
        response = grpc_stub.WhoPing(request)
        assert response.message == f'Hello, the server is pinged by {request.name}!'

    def test_third_ping(self, grpc_stub):
        request = EmptyRequest()
        response = grpc_stub.PingServer(request)
        assert response.message == 'Hello, the server is healthy and it had been pinged 3 times!'
