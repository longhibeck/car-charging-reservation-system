from typing import TypeVar, Self

T = TypeVar("T")


class Result[T]:
    def __init__(
        self,
        is_success: bool,
        value: T | None = None,
        error_messages: list[str] | None = None,
    ):
        self._is_success = is_success
        self._value = value
        self._error_messages = error_messages or []

    @staticmethod
    def success(value: T = None) -> "Result[T]":
        return Result(True, value=value)

    @staticmethod
    def failure(error_messages: str | list[str]) -> "Result[T]":
        messages = (
            error_messages if isinstance(error_messages, list) else [error_messages]
        )
        return Result(False, error_messages=messages)

    def is_success(self) -> bool:
        return self._is_success

    def is_failure(self) -> bool:
        return not self._is_success

    def get_value(self) -> T:
        if not self._is_success:
            raise ValueError("Cannot get value from a failed Result")
        return self._value

    def get_error_messages(self) -> list[str]:
        if self._is_success:
            raise ValueError("Cannot get error messages from a successful Result")
        return self._error_messages
