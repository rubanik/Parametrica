class Configurator:
    
    def __init__(self,path='configuration.cfg'):
        self.raw_config = []
        self.centerlines_configuration = []
        self.plc_paths = []
        self.path = path
        self._headers = ['name','path','setpoint','min','max']

    
    def read_configuration(self):
        try:
            with open(self.path,'r') as cfg:
                data = cfg.readlines()
                self.raw_config = [line.strip().split(',') for line in data]

        except FileNotFoundError as fnf:
            print(f'File at {self.path} not found! ', fnf )

        self.set_cl_configuration(self.raw_config)
        self.set_plc_paths(self.centerlines_configuration)

    def set_cl_configuration(self,raw_config):
        """ Считываем и пишем пути до PLC переменных из конфига """
        for line in raw_config:
            result = dict(zip(self._headers,line))
            self.centerlines_configuration.append(result)

    def set_plc_paths(self,centerlines_configuration):
        """ Считываем и пишем пути до PLC переменных из конфига """
        try:
            for cl in centerlines_configuration:
                if 'path' in cl.keys():
                    self.plc_paths.append(cl['path'])
        except Exception as e:
            print('Ошибка при извлечении пути переменной')


    def get_cl_and_plc_paths(self):
        return self.centerlines_configuration,self.plc_paths
