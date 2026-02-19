from dataclasses import dataclass

import os


@dataclass
class UiConfig:
    base_url: str


@dataclass
class ApiConfig:
    base_url: str


@dataclass
class AuthConfig:
    api: ApiConfig


@dataclass
class ChargingPointsConfig:
    api: ApiConfig


@dataclass
class CarChargingReservationConfig:
    api: ApiConfig
    ui: UiConfig


@dataclass
class SystemTestConfig:
    auth: AuthConfig
    charging_points: ChargingPointsConfig
    car_charging_reservation: CarChargingReservationConfig


class SystemTestConfiguration:
    _config: SystemTestConfig | None = None

    @classmethod
    def load_config(cls):
        if cls._config is None:
            cls._config = SystemTestConfig(
                auth=AuthConfig(
                    api=ApiConfig(os.getenv("AUTH_BASE_URL", "https://dummyjson.com"))
                ),
                charging_points=ChargingPointsConfig(
                    api=ApiConfig(
                        os.getenv("CHARGING_POINTS_BASE_URL", "http://localhost:8081")
                    )
                ),
                car_charging_reservation=CarChargingReservationConfig(
                    api=ApiConfig(
                        os.getenv("SYSTEM_API_BASE_URL", "http://localhost:8080")
                    ),
                    ui=UiConfig(
                        os.getenv("SYSTEM_UI_BASE_URL", "http://localhost:8080")
                    ),
                ),
            )
        return cls._config

    @classmethod
    def get_auth_api_base_url(cls):
        return cls.load_config().auth.api.base_url

    @classmethod
    def get_charging_points_api_base_url(cls):
        return cls.load_config().charging_points.api.base_url

    @classmethod
    def get_system_api_base_url(cls):
        return cls.load_config().car_charging_reservation.api.base_url

    @classmethod
    def get_system_ui_base_url(cls):
        return cls.load_config().car_charging_reservation.ui.base_url
