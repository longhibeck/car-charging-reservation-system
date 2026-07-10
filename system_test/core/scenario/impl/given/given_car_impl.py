from system_test.core.use_case_dsl import UseCaseDsl


class GivenCarImpl:
    """Fluent builder that seeds a car as a test precondition.

    Call exists() to execute add-car, assert success, store the result
    alias, and return to GivenStage for further chaining.

    Example
    -------
    scenario.given().car("car1").with_name("Tesla").exists().when()...
    """

    def __init__(self, app: UseCaseDsl, alias: str, given_stage: "GivenImpl") -> None:
        self._given_stage = given_stage
        self._use_case = app.system().add_car().car_id(alias)

    def with_name(self, value: str) -> "GivenCarImpl":
        self._use_case.name(value)
        return self

    def with_connector_types(self, value: list) -> "GivenCarImpl":
        self._use_case.connector_types(value)
        return self

    def with_battery_charge_limit(self, value: int) -> "GivenCarImpl":
        self._use_case.battery_charge_limit(value)
        return self

    def with_battery_size(self, value: int) -> "GivenCarImpl":
        self._use_case.battery_size(value)
        return self

    def with_max_kw_ac(self, value: int) -> "GivenCarImpl":
        self._use_case.max_kw_ac(value)
        return self

    def with_max_kw_dc(self, value: int) -> "GivenCarImpl":
        self._use_case.max_kw_dc(value)
        return self

    def exists(self) -> "GivenImpl":
        self._use_case.execute().should_succeed()
        return self._given_stage
