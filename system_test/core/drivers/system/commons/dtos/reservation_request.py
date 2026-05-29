from typing import TypedDict
from uuid import UUID


class ReservationRequest(TypedDict):
    car_id: UUID
    user_id: UUID
    charging_point_id: UUID
    start_time: str  # ISO format string
    end_time: str  # ISO format string


class CreateReservationRequest(TypedDict):
    car_id: str
    charging_point_id: str
    start_time: str
    end_time: str
