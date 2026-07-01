from typing import TypedDict
from uuid import UUID

from system_test.core.drivers.system.commons.enums.connector_type import (
    ConnectorTypeLiteral,
)


class GetCarResponse(TypedDict):
    id: UUID
    name: str
    connector_types: list[ConnectorTypeLiteral]
    battery_charge_limit: int
    battery_size: int
    max_kw_ac: int
    max_kw_dc: int


class AddCarResponse(GetCarResponse):
    pass
