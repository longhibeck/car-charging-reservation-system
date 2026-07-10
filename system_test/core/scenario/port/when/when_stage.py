from typing import Protocol

from system_test.core.scenario.port.when.steps.when_add_car import WhenAddCar
from system_test.core.scenario.port.when.steps.when_create_reservation import (
    WhenCreateReservation,
)
from system_test.core.scenario.port.when.steps.when_delete_car import WhenDeleteCar
from system_test.core.scenario.port.when.steps.when_get_reservation import (
    WhenGetReservation,
)
from system_test.core.scenario.port.when.steps.when_list_cars import WhenListCars
from system_test.core.scenario.port.when.steps.when_list_reservations import (
    WhenListReservations,
)
from system_test.core.scenario.port.when.steps.when_login import WhenLogin
from system_test.core.scenario.port.when.steps.when_update_car import WhenUpdateCar


class WhenStage(Protocol):
    """When stage port (mirrors reference structure: when/WhenStage)."""

    def login(self) -> WhenLogin: ...

    def add_car(self) -> WhenAddCar: ...

    def update_car(self) -> WhenUpdateCar: ...

    def delete_car(self) -> WhenDeleteCar: ...

    def list_cars(self) -> WhenListCars: ...

    def create_reservation(self) -> WhenCreateReservation: ...

    def get_reservation(self) -> WhenGetReservation: ...

    def list_reservations(self) -> WhenListReservations: ...
