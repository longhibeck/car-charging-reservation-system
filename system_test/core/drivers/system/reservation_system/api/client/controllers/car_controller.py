from urllib import response
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

    def update_car(
        self,
        car_id: str,
        request: AddCarRequest,
    ) -> Result[None]:
        response = self.http_client.put(f"{self.CARS_PATH}/{car_id}", request)
        return HttpTestUtils.get_ok_result_or_failure(response)        

    def delete_car(self, car_id: str) -> Result[None]:
        response = self.http_client.delete(f"{self.CARS_PATH}/{car_id}")
        return HttpTestUtils.get_no_content_result_or_failure(response)
