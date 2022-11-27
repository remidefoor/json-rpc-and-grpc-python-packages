from mask import Mask

from fee_calculator_pb2 import FeeResponse

app = Mask(__name__)

@app.route(method="CalculateFee", service="FeeCalculator")
def calculate_fee(request):
    return FeeResponse(fee=100)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1020)
