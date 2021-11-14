class CenterLine:

    def __init__(self,name,path,setpoint,plc_variable='', maximum : int=None, minimum : int=None) -> None:
        self.name = name
        self.path = path
        self.setpoint = setpoint
        self.plc_variable = plc_variable 
        self.status = False

        if not maximum and not minimum:
            self.maximum = self.setpoint
            self.minimum = self.setpoint   # Если не задали пределы, то пределы пусть будут равны значению.
        else:
            self.maximum = maximum
            self.minimum = minimum

        if self.plc_variable:
            self.update_status() 


    def __str__(self)-> str:
        return f"CL-'{self.name}'.Setpoint-{self.setpoint}, Path: '{self.path}' Attached to: {self.plc_variable}"
    

    def get_plc_value(self)-> int:
        return int(self.plc_variable.value)


    def update_status(self) -> None:
        """Обновляем статус CL. если мы в пределах или равны уставке то статус ОК(TRUE)"""
        if self.get_plc_value() == self.setpoint or self.in_range():
            self.status = True
        else:
            self.status = False


    def get_str_status(self) -> str:
        if self.status: return 'OK'
        else: return 'NOK'


    def in_range(self) -> bool:
        """Проверяем, в пределах ли мы указанных значений"""
        return self.minimum <= self.get_plc_value() <= self.maximum

    
    def set_plc_variable(self,plc_variable):
            self.plc_variable = plc_variable


class CenterLineList():

    def __init__(self,cl_config):
        self.cl_config = cl_config
        self.cl_list = []
        self.insert_cl_from_config()
        
    def insert_cl_from_config(self):
        for cl in self.cl_config:
            self.cl_list.append(
                CenterLine(
                    cl['name'],
                    cl['path'],
                    cl['setpoint'],
                    minimum=cl['min'],
                    maximum=cl['max']))
    
    def attach_from_conteiner(self,plcvar_list):
        for index,item in enumerate(self.cl_list):
            for plc_var in plcvar_list:
                if item.path == plc_var.name:
                    item.set_plc_variable(plc_var)
        

