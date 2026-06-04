from contextvars import ContextVar

_current_channel: ContextVar[str | None] = ContextVar("channel", default=None)


class ChannelContext:
    @staticmethod
    def set(channel: str) -> None:
        _current_channel.set(channel)

    @staticmethod
    def get() -> str | None:
        return _current_channel.get()

    @staticmethod
    def clear() -> None:
        _current_channel.set(None)
