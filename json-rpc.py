from enum import IntEnum

from flask import Flask
from jsonrpc.backend.flask import api
from jsonrpc.exceptions import JSONRPCInvalidParams

app = Flask(__name__)
app.add_url_rule("/", "api", api.as_view(), methods=["POST"])

GAS_FEE: int = 5


class PackageSize(IntEnum):
    """An enum representing all possible package sizes."""

    LETTER: int = 1
    SMALL: int = 2
    MEDIUM: int = 3
    LARGE: int = 4


@api.dispatcher.add_method
def calculate_fee(package_size: str) -> int:
    """Calculate the gas fee to transport a package.

    :param int package_size: the size of the package
    :return: the gas fee to transport the package
    :rtype: str
    :raises JSONRPCInvalidParams: if the package size does not exist.
    """
    try:
        formatted_package_size: str = package_size.upper()
        package_size_weight: int = PackageSize[formatted_package_size].value
        return GAS_FEE * package_size_weight
    except KeyError:
        raise JSONRPCInvalidParams("The package size does not exist.")
