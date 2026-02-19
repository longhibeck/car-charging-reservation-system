from typing import TypedDict

from system_test.core.drivers.system.commons.enums.connector_type import ConnectorTypeLiteral


class AddCarRequest(TypedDict):
    """Request DTO for adding a new car"""
    name: str
    connector_types: list[ConnectorTypeLiteral]
    battery_charge_limit: int
    battery_size: int
    max_kw_ac: int
    max_kw_dc: int


class UpdateCarRequest(AddCarRequest):
    """Request DTO for updating an existing car - same structure as AddCarRequest"""
    pass
