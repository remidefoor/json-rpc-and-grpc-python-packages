from concurrent import futures
import sys

import grpc

sys.path.append("..")
from services.fee_service import calculate_fee
from fee_calculator_pb2 import FeeRequest, FeeResponse
import fee_calculator_pb2_grpc


class FeeCalculator(
    fee_calculator_pb2_grpc.FeeCalculatorServicer
):
    """gRPC service for calculating fees"""

    def CalculateFee(self, request: FeeRequest, context: grpc.ServicerContext) -> FeeResponse:
        """Handle the remote procedure call to calculate the fee for transporting a package.

        :param FeeRequest request: the request containing the package size, the address of the sender and the address of the receiver
        :param ServicerContext context: the context of the request
        :return: the fee to transport the package
        :rtype: FeeResponse
        :raises grpc._channel._InactiveRpcError: if the package size does not exist
        """
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
    """Start the gRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fee_calculator_pb2_grpc.add_FeeCalculatorServicer_to_server(FeeCalculator(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
