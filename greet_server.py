from concurrent import futures
import grpc
import greet_pb2
import greet_pb2_grpc
import time


class Greetservicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print("SayHello Request made")
        print(request)

        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"

        return hello_reply
    
    def ParrotSaysHello(self, request, context):
        print("ParrotSaysHello Request made")
        print(request)

        for i in range(3):
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"Parrot says: {request.greeting} {request.name} {i +1}"
            yield hello_reply
            time.sleep(3)

    def User(self, request, context):
        response_message = f"Hello {request.name}, your email is {request.email}, your age is {request.age}."
        return greet_pb2.UserReply(message=response_message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(Greetservicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
