from typing import TypedDict
from uuid import UUID
from system_test.core.drivers.system.commons.enums.reservation_status import (
    ReservationStatusLiteral,
)


class ReservationResponse(TypedDict):
    id: UUID
    car_id: UUID
    user_id: UUID
    charging_point_id: UUID
    start_time: str  # ISO format string
    end_time: str  # ISO format string
    status: ReservationStatusLiteral
    created_at: str  # ISO format string
    updated_at: str  # ISO format string
