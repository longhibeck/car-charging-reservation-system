from typing import TypeVar
from system_test.core.drivers.commons.result import Result

T = TypeVar("T")


def to_be_success(result: Result[T]) -> T:
    """
    Assert that the result is successful and return its value.
    
    Returns:
        The value contained in the successful result
        
    Raises:
        AssertionError: If the result is a failure
    """
    if not result.is_success():
        error_messages = result.get_error_messages()
        error_text = ", ".join(error_messages) if error_messages else "Unknown error"
        raise AssertionError(f"Expected result to be successful, but it failed with: {error_text}")
    return result.get_value()


def to_be_failure_with(result: Result[T], expected_message: str) -> None:
    """
    Assert that the result is a failure and contains the expected error message.
    
    Args:
        result: The Result object to check
        expected_message: A substring that should appear in the error messages
        
    Raises:
        AssertionError: If the result is successful or doesn't contain the expected message
    """
    if not result.is_failure():
        value = result.get_value()
        raise AssertionError(f"Expected result to be a failure, but it succeeded with value: {value}")
    
    error_messages = result.get_error_messages()
    
    # Check if any error message contains the substring
    if not any(expected_message in msg for msg in error_messages):
        actual_messages = ", ".join(error_messages)
        raise AssertionError(
            f"Expected error messages to contain '{expected_message}'. "
            f"Actual error messages: {actual_messages}"
        )