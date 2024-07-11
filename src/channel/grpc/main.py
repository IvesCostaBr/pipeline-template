from dotenv import load_dotenv
import os

if os.environ.get("DEPLOY") and bool(int(os.environ.get("DEPLOY"))):
    from src.utils.secrets import start_secret_env

    if os.path.exists("./src/configs/credential-gcp.json"):
        start_secret_env()

load_dotenv()

import grpc
from concurrent import futures

def serve(port: int = 50051):
    # server_credentials = grpc.ssl_server_credentials(
    #     [(open('./src/configs/server.crt', 'rb').read(), open('./src/configs/server.key', 'rb').read())]
    # )
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # notifier_pb2_grpc.add_NotifierServicer_to_server(
    #     dispatch.DispatchServicer(), server
    # )

    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Server started at [::]:{port}")
    server.wait_for_termination()


if __name__ == "__main__":
    if os.environ.get("ENVIRONMENT") != "DEV":
        # os.remove(".env")
        pass
    serve(int(os.environ.get("GRPC_PORT", 50051)))
