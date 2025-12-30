from typing import TypedDict


class ReservationResponse(TypedDict):
    """Response DTO for Reservation entity"""
    id: int
    car_id: int
    user_id: int
    charging_point_id: str
    start_time: str  # ISO format string
    end_time: str    # ISO format string
    status: str
    created_at: str  # ISO format string
    updated_at: str  # ISO format string
