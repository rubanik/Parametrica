class CenterLine:
    def __init__(self,name,setpoint,plc_variable, maximum : int=None, minimum : int=None) -> None:
        self.name = name
        self.setpoint = setpoint
        self.plc_variable = plc_variable 
        self.status = False

        if not maximum and not minimum:
            self.maximum = self.setpoint
            self.minimum = self.setpoint   # Если не задали пределы, то пределы пусть будут равны значению.
        else:
            self.maximum = maximum
            self.minimum = minimum

        self._status()

    def __str__(self)-> str:
        return f"CL-'{self.name}'.Setpoint-{self.setpoint}. PLC Value-{self.get_plc_value()}. Status-{self.get_str_status()}"
    

    def get_plc_value(self)-> int:
        return int(self.plc_variable.value)


    def update_status(self) -> None:
        if self.get_plc_value() == self.setpoint or self.in_range():
            self.status = True
        else:
            self.status = False


    def get_str_status(self) -> str:
        if self.status: return 'OK'
        else: return 'NOK'


    def in_range(self) -> bool:
        return self.minimum <= self.get_plc_value() <= self.maximum        