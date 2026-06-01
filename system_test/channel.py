import pytest
from system_test.core.channel_type import ChannelType  # re-export for convenience


def channel(*channels: str) -> pytest.MarkDecorator:
    """
    Mark a test to run once for each specified channel.

    Example::

        @channel(ChannelType.API, ChannelType.UI)
        def test_should_login(self) -> None: ...

    Set the CHANNEL env var to run only one channel (case-insensitive)::

        CHANNEL=API pytest tests/
    """
    if not channels:
        raise ValueError("@channel requires at least one channel type.")
    return pytest.mark.channel(base_channels=tuple(channels))


__all__ = ["channel", "ChannelType"]
