from system_test.core.system_test_configuration import SystemTestConfiguration
from system_test.core.drivers.system.reservation_system.api.system_api_driver import SystemApiDriver
from system_test.core.drivers.system.reservation_system.ui.system_ui_driver import SystemUiDriver
from system_test.core.drivers.external.charging_points.charging_points_api_driver import ChargingPointsDriver
from system_test.core.drivers.external.auth.auth_api_driver import AuthApiDriver

class DriverFactory:

    @staticmethod
    def create_system_ui_driver():
        return SystemUiDriver(SystemTestConfiguration.get_system_ui_base_url())
            
    @staticmethod
    def create_system_api_driver():
        return SystemApiDriver(SystemTestConfiguration.get_system_api_base_url())
    
    @staticmethod
    def create_charging_points_api_driver():
        return ChargingPointsDriver(SystemTestConfiguration.get_charging_points_api_base_url())
    
    @staticmethod
    def create_auth_api_driver():
        return AuthApiDriver(SystemTestConfiguration.get_auth_api_base_url())