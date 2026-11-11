from importlib.metadata import PackageNotFoundError
from importlib.metadata import version


def package_version(package_name: str) -> str:
    """Return the version of an installed package.

    :param package_name: Name of the distribution, or of a sub package.
    :returns: The installed version, or ``-`` when no name is given.
    """
    if not package_name:
        return "-"
    try:
        installed: str = version(package_name)
    except PackageNotFoundError:
        # Probably a sub package (i.e. portalbrasil.legislativo.testing)
        package_name = (
            ".".join(package_name.split(".")[:-1]) if "." in package_name else ""
        )
        return package_version(package_name)
    return installed
