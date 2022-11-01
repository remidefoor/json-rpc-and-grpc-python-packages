from concurrent import futures
import sys

import grpc

# set path
sys.path.append("..")
from fee_service import calculate_fee
from fee_calculator_pb2 import FeeResponse
import fee_calculator_pb2_grpc


class FeeCalculator(
    fee_calculator_pb2_grpc.FeeCalculatorServicer
):
    def CalculateFee(self, request, context):
        try:
            fee: int = calculate_fee(
                request.package_size,
                request.src,
                request.dest
            )
            return FeeResponse(fee=fee)
        except:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "The package size does not exist.")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fee_calculator_pb2_grpc.add_FeeCalculatorServicer_to_server(FeeCalculator(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
