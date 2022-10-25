from enum import Enum

from flask import Flask
from jsonrpc.backend.flask import api

app = Flask(__name__)
app.add_url_rule("/", "api", api.as_view(), methods=["POST"])

GAS_FEE: int = 5


class PackageSize(Enum):
    LETTER = 1
    SMALL = 2
    MEDIUM = 3
    LARGE = 4


@api.dispatcher.add_method
def calculate_fee(package_size: str):
    formatted_package_size = package_size.upper()
    try:
        return GAS_FEE * PackageSize[formatted_package_size].value
    except:
        return 0
