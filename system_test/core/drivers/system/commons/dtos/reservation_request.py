from typing import TypedDict


class ReservationRequest(TypedDict):
    car_id: str
    charging_point_id: str
    start_time: str  # ISO format string
    end_time: str  # ISO format string


class CreateReservationRequest(TypedDict):
    car_id: str
    charging_point_id: str
    start_time: str
    end_time: str
