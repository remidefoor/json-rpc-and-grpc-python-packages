from enum import IntEnum

FEE: int = 5


class PackageSize(IntEnum):
    """An enum representing all possible package sizes."""

    LETTER: int = 1
    SMALL: int = 2
    MEDIUM: int = 3
    LARGE: int = 4


def calculate_fee(package_size: str, src: float, dest: float) -> int:
    """Calculate the fee to transport a package.

    :param int package_size: the size of the package
    :param float src: the address of the sender
    :param float dest: the address of the receiver
    :return: the fee to transport the package
    :rtype: int
    :raises KeyError: if the package size does not exist.
    """
    formatted_package_size: str = package_size.upper()
    package_size_weight: int = PackageSize[formatted_package_size].value
    return FEE * package_size_weight
