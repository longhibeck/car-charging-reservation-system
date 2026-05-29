from typing import TypedDict

class GetChargingPointResponse(TypedDict):
    id: str
    name: str
    status: str
    connector_type: str
    charging_type: str
    max_power_kw: int