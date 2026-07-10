from system_test.core.scenario.impl.when.when_add_car_impl import WhenAddCarImpl
from system_test.core.scenario.impl.when.when_create_reservation_impl import (
    WhenCreateReservationImpl,
)
from system_test.core.scenario.impl.when.when_delete_car_impl import WhenDeleteCarImpl
from system_test.core.scenario.impl.when.when_get_reservation_impl import (
    WhenGetReservationImpl,
)
from system_test.core.scenario.impl.when.when_list_cars_impl import WhenListCarsImpl
from system_test.core.scenario.impl.when.when_list_reservations_impl import (
    WhenListReservationsImpl,
)
from system_test.core.scenario.impl.when.when_login_impl import WhenLoginImpl
from system_test.core.scenario.impl.when.when_update_car_impl import WhenUpdateCarImpl
from system_test.core.use_case_dsl import UseCaseDsl


class WhenStageImpl:
    """Concrete WhenStage: factory for all when step implementations.

    Example
    -------
    scenario.when().add_car().with_name("Tesla").then().should_succeed()
    scenario.when().create_reservation().car_id("car1")...then().should_succeed()
    """

    def __init__(self, app: UseCaseDsl) -> None:
        self._app = app

    def login(self) -> WhenLoginImpl:
        return WhenLoginImpl(self._app)

    def add_car(self) -> WhenAddCarImpl:
        return WhenAddCarImpl(self._app)

    def update_car(self) -> WhenUpdateCarImpl:
        return WhenUpdateCarImpl(self._app)

    def delete_car(self) -> WhenDeleteCarImpl:
        return WhenDeleteCarImpl(self._app)

    def list_cars(self) -> WhenListCarsImpl:
        return WhenListCarsImpl(self._app)

    def list_reservations(self) -> WhenListReservationsImpl:
        return WhenListReservationsImpl(self._app)

    def create_reservation(self) -> WhenCreateReservationImpl:
        return WhenCreateReservationImpl(self._app)

    def get_reservation(self) -> WhenGetReservationImpl:
        return WhenGetReservationImpl(self._app)
