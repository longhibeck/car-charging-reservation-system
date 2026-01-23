from typing import TypedDict

class ReservationRequest(TypedDict):
    """Request DTO for creating a Reservation"""
    car_id: int
    user_id: int
    charging_point_id: str
    start_time: str  # ISO format string
    end_time: str    # ISO format string