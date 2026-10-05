import pkg_resources


def package_version(package_name: str) -> str:
    """Return the version of an installed package."""
    if not package_name:
        return "-"
    try:
        package_dist = pkg_resources.get_distribution(package_name)
    except pkg_resources.DistributionNotFound:
        # Probably a sub package (i.e. portalbrasil.legislativo.testing)
        package_name = (
            ".".join(package_name.split(".")[:-1]) if "." in package_name else ""
        )
        return package_version(package_name)
    version: str = package_dist.version
    return version
