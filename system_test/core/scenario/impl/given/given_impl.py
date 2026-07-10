from system_test.core.scenario.impl.given.given_car_impl import GivenCarImpl
from system_test.core.scenario.impl.given.given_reservation_impl import (
    GivenReservationImpl,
)
from system_test.core.scenario.impl.when.when_stage_impl import WhenStageImpl
from system_test.core.use_case_dsl import UseCaseDsl


class GivenImpl:
    """Concrete GivenStage: sets up preconditions before the action.

    Immediate steps (user_is_logged_in) execute right away and return self
    for chaining. Builder steps (car, reservation) return a fluent object
    committed by calling .exists(), which also returns self.
    Call when() to transition to the action stage.

    Example
    -------
    scenario.given()
        .user_is_logged_in()
        .car("car1").exists()
        .reservation("res1").for_car("car1").on_charging_point(CP_ID).exists()
        .when().get_reservation().reservation_id("res1")
        .then().should_succeed().has_status("active")
    """

    def __init__(self, app: UseCaseDsl) -> None:
        self._app = app

    # ------------------------------------------------------------------
    # Immediate setup
    # ------------------------------------------------------------------

    def user_is_logged_in(
        self,
        username: str = "addisonw",
        password: str = "addisonwpass",
    ) -> "GivenImpl":
        self._app.system().login().username(username).password(
            password
        ).execute().should_succeed()
        return self

    # ------------------------------------------------------------------
    # Builder steps
    # ------------------------------------------------------------------

    def car(self, alias: str) -> GivenCarImpl:
        return GivenCarImpl(self._app, alias, self)

    def reservation(self, alias: str) -> GivenReservationImpl:
        return GivenReservationImpl(self._app, alias, self)

    # ------------------------------------------------------------------
    # Stage transitions
    # ------------------------------------------------------------------

    def when(self) -> WhenStageImpl:
        return WhenStageImpl(self._app)

    def then(self) -> object:
        raise NotImplementedError(
            "Direct then() on GivenStage is not yet implemented. "
            "Reach then() through a when() step."
        )
