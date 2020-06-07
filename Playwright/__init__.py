__version__ = "0.1.0"
import grpc  # type: ignore

import Playwright.generated.playwright_pb2 as playwright_pb2
import Playwright.generated.playwright_pb2_grpc as playwright_pb2_grpc


class Playwright:
    @staticmethod
    def open_browser():
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = playwright_pb2_grpc.PlaywrightStub(channel)
            stub.OpenBrowser(playwright_pb2.Empty())

    @staticmethod
    def close_browser():
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = playwright_pb2_grpc.PlaywrightStub(channel)
            stub.CloseBrowser(playwright_pb2.Empty())