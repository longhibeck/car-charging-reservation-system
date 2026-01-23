from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.system.commons.dtos.car_request import AddCarRequest
from system_test.core.drivers.system.commons.dtos.car_response import AddCarResponse
from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.commons.clients.http_test_utils import HttpTestUtils


class CarController:
    CARS_PATH = "/api/v1/cars"

    def __init__(self, http_client: HttpTestClient):
        self.http_client = http_client

    def add_car(self, request: AddCarRequest) -> Result[AddCarResponse]:
        response = self.http_client.post(f"{self.CARS_PATH}/", request)
        return HttpTestUtils.get_created_result_or_failure(response)
    
    def list_cars(self) -> Result[list[AddCarResponse]]:
        response = self.http_client.get(f"{self.CARS_PATH}/")
        return HttpTestUtils.get_ok_result_or_failure(response)
    
    def get_car(self, car_id: str) -> Result[AddCarResponse]:
        response = self.http_client.get(f"{self.CARS_PATH}/{car_id}")
        return HttpTestUtils.get_ok_result_or_failure(response)


"""
    def list_cars(self) -> httpx.Response:
        return self.http_client.get(f"{self.CARS_PATH}/")

    def get_car(self, car_id: str) -> httpx.Response:
        return self.http_client.get(f"{self.CARS_PATH}/{car_id}")

    def update_car(
        self,
        car_id: int,
        name: str,
        connector_types: list[ConnectorTypeLiteral],
        battery_charge_limit: int,
        battery_size: int,
        max_kw_ac: int,
        max_kw_dc: int,
    ) -> httpx.Response:
        request: UpdateCarRequest = {
            "name": name,
            "connector_types": connector_types,
            "battery_charge_limit": battery_charge_limit,
            "battery_size": battery_size,
            "max_kw_ac": max_kw_ac,
            "max_kw_dc": max_kw_dc,
        }
        return self.http_client.put(f"{self.ENDPOINT}/{car_id}", request)

    def delete_car(self, car_id: int) -> httpx.Response:
        return self.http_client.post(f"{self.ENDPOINT}/{car_id}/delete")

"""
