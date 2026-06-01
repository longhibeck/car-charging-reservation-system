from system_test.core.system_test_configuration import SystemTestConfiguration
from system_test.core.drivers.system.reservation_system.api.system_api_driver import SystemApiDriver
from system_test.core.drivers.system.reservation_system.ui.system_ui_driver import SystemUiDriver
from system_test.core.drivers.external.charging_points.charging_points_api_driver import ChargingPointsApiDriver
from system_test.core.drivers.external.auth.auth_api_driver import AuthApiDriver
from system_test.core.channel_context import ChannelContext
from system_test.core.channel_type import ChannelType


class DriverFactory:

    @staticmethod
    def create_system_ui_driver():
        return SystemUiDriver(SystemTestConfiguration.get_system_ui_base_url())

    @staticmethod
    def create_system_api_driver():
        return SystemApiDriver(SystemTestConfiguration.get_system_api_base_url())

    @staticmethod
    def create_system_driver_for_current_channel():
        """
        Create the system driver that matches the channel set by @channel().

        Use this inside tests or BaseE2eTest.create_system_driver() when the
        test class is annotated with @channel(ChannelType.API, ChannelType.UI).
        """
        channel = ChannelContext.get()
        if channel == ChannelType.UI:
            return DriverFactory.create_system_ui_driver()
        # Default / API channel
        return DriverFactory.create_system_api_driver()

    @staticmethod
    def create_charging_points_api_driver():
        return ChargingPointsApiDriver(SystemTestConfiguration.get_charging_points_api_base_url())

    @staticmethod
    def create_auth_api_driver():
        return AuthApiDriver(SystemTestConfiguration.get_auth_api_base_url())