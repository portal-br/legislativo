from typing import TypedDict


class DistributionInfo(TypedDict):
    """Distribution Information."""

    name: str
    title: str
    package_name: str
    package_version: str
