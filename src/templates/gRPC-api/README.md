# Project Name

### Overview

### Installation

### Local Development

To run the code locally, first install the dependencies into a virtual environment. 
The following commands will install the dependencies on Windows:

````shell
python -m venv venv

<Working-Directory>\venv\Scripts\activate.bat

(venv) <Working-Directory>  python -m pip install -r requirements.txt
````

Now, to generate Python code from the protobufs, navigate to `src\server` directory and run the following command:

```shell
 python -m grpc_tools.protoc -I ../../protobufs --python_out=../stubs --grpc_python_out=../stubs ../../protobufs/*.proto
```
Here’s a breakdown: 
- **python -m grpc_tools.protoc** runs the protobuf compiler, which will generate Python code from the protobuf code.

- **-I ../../protobufs** tells the compiler where to find files that your protobuf code imports. You don’t actually use the import feature, but the -I flag is required nonetheless.

- **--python_out=../stubs --grpc_python_out=../stubs** tells the compiler where to output the Python files. In this template we generate all the compiled code under the a `stubs` to group tham and to use the same for the client and the server.

- **../protobufs/\*.proto** is the path to the protobuf file, which will be used to generate the Python code. By using a regex (`*.proto`), we indicates that all protobuf files will be compiled.

The generated files include Python types and functions to interact with your API.


#### Debugging

To explore the running API you can either use a code based client or client tools such us [BoomRPC](https://github.com/bloomrpc/bloomrpc)

### Build

### Deployment

Docker is perfect for deploying a Python microservice because you can package all the dependencies and run 
the microservice in an isolated environment

##### Using docker CLI

````shell
docker build . -f docker/Dockerfile -t <your-tag>
````

````shell
docker run -p 127.0.0.1:50056:50051/tcp <your-tag>
````
##### Using docker-compose

````shell
docker-compose build
````

````shell
docker-compose up -d 
````
