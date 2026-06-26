from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.system.add_car import AddCar
from system_test.core.dsl.system.create_reservation import CreateReservation
from system_test.core.dsl.system.delete_car import DeleteCar
from system_test.core.dsl.system.get_reservation import GetReservation
from system_test.core.dsl.system.go_to_system import GoToSystem
from system_test.core.dsl.system.list_cars import ListCars
from system_test.core.dsl.system.list_reservations import ListReservations
from system_test.core.dsl.system.login import Login
from system_test.core.dsl.system.update_car import UpdateCar


class SystemDsl:
    """Domain DSL for the car-charging reservation system.

    One factory method per use case — no logic here, only creation.

    Example
    -------
    app.system().go_to_system().execute().should_succeed()
    app.system().login().username("addisonw").password("pass").execute().should_succeed()
    app.system().add_car().car_id("car1").name("BYD Seal U")...execute().should_succeed()
    app.system().create_reservation().car_id("car1")...execute().should_succeed()
    """

    def __init__(self, driver: SystemDriver, context: UseCaseContext) -> None:
        self._driver = driver
        self._context = context

    def go_to_system(self) -> GoToSystem:
        return GoToSystem(self._driver, self._context)

    def login(self) -> Login:
        return Login(self._driver, self._context)

    def add_car(self) -> AddCar:
        return AddCar(self._driver, self._context)

    def update_car(self) -> UpdateCar:
        return UpdateCar(self._driver, self._context)

    def delete_car(self) -> DeleteCar:
        return DeleteCar(self._driver, self._context)

    def list_cars(self) -> ListCars:
        return ListCars(self._driver, self._context)

    def list_reservations(self) -> ListReservations:
        return ListReservations(self._driver, self._context)

    def create_reservation(self) -> CreateReservation:
        return CreateReservation(self._driver, self._context)

    def get_reservation(self) -> GetReservation:
        return GetReservation(self._driver, self._context)
