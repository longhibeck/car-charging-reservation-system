import pytest


def channel(*channels: str) -> pytest.MarkDecorator:
    if not channels:
        raise ValueError("@channel requires at least one channel type.")
    return pytest.mark.channel(base_channels=tuple(channels))
