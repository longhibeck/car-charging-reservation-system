from typing import TypedDict

from system_test.core.clients.system.api.enums.connector_type import ConnectorTypeLiteral


class CreateCarRequest(TypedDict):
    """Request DTO for creating a new car"""
    name: str
    connector_types: list[ConnectorTypeLiteral]
    battery_charge_limit: int
    battery_size: int
    max_kw_ac: int
    max_kw_dc: int


class UpdateCarRequest(CreateCarRequest):
    """Request DTO for updating an existing car - same structure as CreateCarRequest"""
    pass
