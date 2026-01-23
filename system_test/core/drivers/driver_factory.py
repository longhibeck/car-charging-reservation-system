from system_test.core.system_test_configuration import SystemTestConfiguration
from system_test.core.drivers.system.reservation_system.api.reservation_system_api_driver import SystemApiDriver
#from system_test.core.drivers.system.reservation_system.ui.reservation_system_ui_driver import SystemUiDriver


class DriverFactory:

 #   @staticmethod
 #   def create_system_ui_driver():
 #       return SystemUiDriver(conf)    
            
    @staticmethod
    def create_system_api_driver():
        return SystemApiDriver(SystemTestConfiguration.get_car_charging_reservation_api_base_url())
    
    #def create_