from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.shared.void_verification import VoidVerification


class DeleteCar:
    """Use case: delete an existing car.

    car_id() resolves from the context result map — pass the same alias
    used in the preceding add_car() call.

    Example
    -------
    app.system().delete_car().car_id("car1").execute().should_succeed()
    """

    def __init__(self, driver: SystemDriver, context: UseCaseContext) -> None:
        self._driver = driver
        self._context = context
        self._car_id_alias: str | None = None

    def car_id(self, alias: str) -> "DeleteCar":
        self._car_id_alias = alias
        return self

    def execute(self) -> UseCaseResult[None, VoidVerification]:
        car_id = self._context.get_result_value(self._car_id_alias)
        result = self._driver.delete_car(car_id=car_id)
        return UseCaseResult(result, self._context, VoidVerification)
