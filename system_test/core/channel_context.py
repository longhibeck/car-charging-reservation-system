from contextvars import ContextVar

_current_channel: ContextVar[str | None] = ContextVar("channel", default=None)


class ChannelContext:
    """
    Holds the channel type for the currently executing test.

    Mirrors ChannelContext from the optivem-testing library (Java / TypeScript).
    Uses a ContextVar so it is coroutine-safe and thread-safe.

    Usage inside a driver or test helper:
        from system_test.core.channel_context import ChannelContext

        channel = ChannelContext.get()   # "API" | "UI" | None
    """

    @staticmethod
    def set(channel: str) -> None:
        _current_channel.set(channel)

    @staticmethod
    def get() -> str | None:
        return _current_channel.get()

    @staticmethod
    def clear() -> None:
        _current_channel.set(None)
