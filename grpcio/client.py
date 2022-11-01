import grpc

from fee_calculator_pb2 import FeeRequest
from fee_calculator_pb2_grpc import FeeCalculatorStub

channel = grpc.insecure_channel("localhost:50051")
client = FeeCalculatorStub(channel)
req: FeeRequest = FeeRequest(
    package_size="letter",
    src=0.0,
    dest=1.1
)
fee: int = client.CalculateFee(req)
print(fee)
