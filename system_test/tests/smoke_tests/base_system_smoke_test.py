import pytest
from system_test.core.drivers.commons.result_assert import ResultAssert
from system_test.core.drivers.commons.result import Result
from abc import ABC, abstractmethod
from functools import wraps


def login_as(username: str = "addisonw", password: str = "addisonwpass"):
    """Decorator that automatically logs in before executing the test method."""
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = self.driver.login(username, password)
            self.assert_that(result).is_success()
            return func(self, *args, **kwargs)
        return wrapper
    return decorator


class BaseSystemTest(ABC):

    @abstractmethod
    def create_driver(self):
        ...

    @pytest.fixture(autouse=True)
    def setup_driver(self):
        self.driver = self.create_driver()
        yield

    # shared test helpers
    def assert_that(self, result: Result) -> ResultAssert:
        """Fluent assertion method for Result objects."""
        return ResultAssert.assert_that_result(result)
    
    # Maybe remove
    def assert_success(self, result: Result):
        """Convenience method to assert success."""
        self.assert_that(result).is_success()