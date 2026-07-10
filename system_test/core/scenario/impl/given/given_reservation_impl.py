from system_test.core.use_case_dsl import UseCaseDsl


class GivenReservationImpl:
    """Fluent builder that seeds a reservation as a test precondition.

    Call exists() to execute create-reservation, assert success, store the
    result alias, and return to GivenStage for further chaining.

    Example
    -------
    scenario.given()
        .car("car1").exists()
        .reservation("res1").for_car("car1").on_charging_point(CP_ID).exists()
        .when()...
    """

    def __init__(self, app: UseCaseDsl, alias: str, given_stage: "GivenImpl") -> None:
        self._given_stage = given_stage
        self._use_case = app.system().create_reservation().reservation_id(alias)

    def for_car(self, alias: str) -> "GivenReservationImpl":
        self._use_case.car_id(alias)
        return self

    def on_charging_point(self, value: str) -> "GivenReservationImpl":
        self._use_case.charging_point_id(value)
        return self

    def from_time(self, value: str) -> "GivenReservationImpl":
        self._use_case.start_time(value)
        return self

    def to_time(self, value: str) -> "GivenReservationImpl":
        self._use_case.end_time(value)
        return self

    def exists(self) -> "GivenImpl":
        self._use_case.execute().should_succeed()
        return self._given_stage
