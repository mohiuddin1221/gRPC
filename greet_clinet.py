import grpc
import greet_pb2
import greet_pb2_grpc


def run_sayhello():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        request = greet_pb2.HelloRequest(greeting="Hello", name="John")
        response = stub.SayHello(request)
        print("Greeter client received: " + response.message)

def run_parrot_says_hello():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        request = greet_pb2.HelloRequest(greeting="Parrot says", name="Hello")
        responses = stub.ParrotSaysHello(request)
        for response in responses:
           print("Greeter client received: " + response.message)


if __name__ == "__main__":
    run_sayhello()
    run_parrot_says_hello()

