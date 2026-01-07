from typing import TypedDict


class CarResponse(TypedDict):
    """Response DTO for Car entity"""
    id: int
    name: str
    connector_types: list[str]
    battery_charge_limit: int
    battery_size: int
    max_kw_ac: int
    max_kw_dc: int

