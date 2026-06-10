import os

import pytest

from system_test.core.channels.channel_context import ChannelContext


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line(
        "markers",
        "channel(base_channels): run the test once per channel",
    )


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    marker = metafunc.definition.get_closest_marker("channel")
    if marker is None:
        return

    channels = list(marker.kwargs["base_channels"])

    env = os.getenv("CHANNEL")
    if env:
        channels = [c for c in channels if c.lower() == env.lower()] or channels

    metafunc.parametrize(
        "_channel_ctx",
        channels,
        indirect=True,
        ids=[c.lower() for c in channels],
    )


@pytest.fixture(autouse=True)
def _channel_ctx(request: pytest.FixtureRequest):
    if not hasattr(request, "param"):
        yield
        return

    ChannelContext.set(request.param)
    yield request.param
    ChannelContext.clear()
