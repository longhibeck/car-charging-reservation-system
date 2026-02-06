class ResultAssertionError(AssertionError): ...


class ResultAssert:
    def __init__(self, actual):
        self.actual = actual

    @staticmethod
    def assert_that_result(actual):
        return ResultAssert(actual)

    def is_success(self):
        if self.actual is None:
            raise ResultAssertionError("Result was None")

        if not self.actual.is_success():
            raise ResultAssertionError(
                f"Expected result to be success but was failure with errors: "
                f"{self.actual.get_error_messages()}"
            )

        return self

    def is_failure(self, error_message=None):
        if self.actual is None:
            raise ResultAssertionError("Result was None")

        if not self.actual.is_failure():
            raise ResultAssertionError("Expected result to be failure but was success")

        if error_message is not None:
            errors = self.actual.get_error_messages()
            if error_message not in errors:
                raise ResultAssertionError(
                    f"Expected result to contain error '{error_message}' "
                    f"but errors were: {errors}"
                )

        return self
