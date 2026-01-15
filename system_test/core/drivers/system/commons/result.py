from typing import TypeVar, Self

T = TypeVar("T")


class Result:
    def __init__(
        self, success: bool, value: T | None = None, error_messages: list[str] | None = None 
    ):
        self.success = success
        self.value = value
        self.error_messages = error_messages or []

    @staticmethod
    def success(value: T) -> Self:
        return Result(True, value=value)

    @staticmethod
    def failure(error_messages: str | list[str]) -> Self:
        messages = error_messages if isinstance(error_messages, list) else [error_messages]
        return Result(False, error_messages=messages)

    def is_success(self) -> bool:
        return self.success

    def is_failure(self) -> bool:
        return not self.success

    def get_value(self) -> T:
        if not self.success:
            raise ValueError("Cannot get value from a failed Result")
        return self.value 

    def get_error_messages(self) -> list[str]:
        if self.success:
            raise ValueError("Cannot get error messages from a successful Result")
        return self.error_messages
