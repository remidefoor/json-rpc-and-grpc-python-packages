import sys

from flask import Flask
from jsonrpc import exceptions
from jsonrpc.backend.flask import api

sys.path.append("..")
from services.fee_service import calculate_fee

app = Flask(__name__)
app.add_url_rule("/", "api", api.as_view(), methods=["POST"])


@api.dispatcher.add_method(name="calculate_fee")
def fee_request_handler(package_size: str, src: float, dest: float) -> int:
    """Handle the remote procedure call to calculate the fee for transporting a package.

    :param int package_size: the size of the package
    :param float src: the address of the sender
    :param float dest: the address of the receiver
    :return: the fee to transport the package
    :rtype: int
    :raises JSONRPCInvalidParams: if the package size does not exist
    """
    try:
        return calculate_fee(package_size, src, dest)
    except KeyError:
        raise exceptions.JSONRPCInvalidParams("The package size does not exist.")
