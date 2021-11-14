import pyads

class PlcVariable:
    """
    This class contains plc.variable information:
    path, status, value, name.
    """

    def __init__(self,name:str,value:int,plc) -> None:
        self.name = name
        self.value = value
        self.plc = plc
        self.history = [self.value]


    def __str__(self) -> str:
        return f"Name: {self.name}, Value: {self.value}"


    def diff_checking(func):
        """ Декоратор в котором сверяется прошлое значение переменной и нынешнее"""
        def checnking(self):
            prev_value = self.value

            func(self)
            
            if prev_value != self.value:
                print(f'{TimeStamp().get_time_stamp()} - Value of {self.name} has been changed from {prev_value} to {self.value}')
                self.history.append(self.value) # Добавляем новое значение в history, типа отслеживаем изменение
                print(f'History: {self.history}<--Now')
        return checnking


    def get_name(self):
        return self.name


    def get_value(self):
        return self.value

    @diff_checking
    def update_value(self):
        self.value = self.plc.read_by_name(self.name,pyads.PLCTYPE_INT)  


class VariableContainer:
    """
    В контейнер собираем все переменные. Обновляем их и проверяем статус.
    """
    def __init__(self,plc) -> None:
        self.container = []
        self.plc = plc

    def __str__(self) -> str:
        """ Container str representation """
        return f'Container:\n {self.container}'

    def get_names(self)-> list:
        """ Return a list of variables names\paths are contained in the container """
        return [variable.name for variable in self.container]

    def add_to_container(self,plc_variable):
        """ Add new PlcVariable instance into container"""
        self.container.append(plc_variable)

    def show_container(self) -> None:
        """
        Print the contents of the container
        It looks like: "'Name' 100"
        """
        for plc_variable in self.container:
            print(plc_variable.name,plc_variable.value)
    
    def update_container(self):
        """
        ***NOT USED***
        Refresh all values in the container's PLC variables
        Use pyads.Connection.read_list_by_name - method
        But may be it's better to read values from the plc one by one.
        TODO: check it. Compare these two ways.
        """
        if self.container:
            values = self.plc.read_list_by_name(container.get_names())
            self.container = []
            for name in values:
                self.add_to_container(PlcVariable(
                                        name=name,
                                        value=values[name],
                                        plc=self.plc))
            return self.container
    
    def update_variables(self)-> None:
        """ Update all the conteiner's variables one by one with PlcVariable.update_value()"""
        if self.container:
            for item in self.container:
                item.update_value()

    def get_plcvariales(self):
        return self.container
