

class DriverFactory:

    @staticmethod
    def create_system_ui_driver():
        return SystemUiDriver(conf)    
            
    @staticmethod
    def create_system_api_driver():
        return SystemApiDriver(conf)
    
    def create_