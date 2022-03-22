FROM python

RUN mkdir /service
COPY ../protobufs/ /service/protobufs/
COPY ../src/ /service/
COPY requirements.txt /service/
WORKDIR /service/
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ./protobufs --python_out=./stubs \
           --grpc_python_out=./stubs ./protobufs/*.proto

EXPOSE 50051
ENTRYPOINT [ "python", "server.py" ]