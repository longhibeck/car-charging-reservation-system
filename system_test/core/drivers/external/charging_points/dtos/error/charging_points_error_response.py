from typing import TypedDict, NotRequired


class ChargingPointsErrorResponse(TypedDict):
    message: str
    id: NotRequired[str]
