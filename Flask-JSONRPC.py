from services.fee_service import calculate_fee

from flask import Flask
from flask_jsonrpc import JSONRPC, exceptions

app = Flask(__name__)
jsonrpc = JSONRPC(app, "/", enable_web_browsable_api=True)


@jsonrpc.method("calculate_fee")
def fee_request_handler(package_size: str, src: float, dest: float) -> int:
    """Handle the remote procedure call to calculate the fee for transporting a package.

        :param int package_size: the size of the package
        :param float src: the address of the sender
        :param float dest: the address of the receiver
        :return: the fee to transport the package
        :rtype: int
        :raises InvalidParamsError: if the package size does not exist.
        """
    try:
        return calculate_fee(package_size, src, dest)
    except KeyError:
        raise exceptions.InvalidParamsError(
            message="The package size does not exist.",
            data=package_size
        )
