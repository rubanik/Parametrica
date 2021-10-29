import datetime

class TimeStamp:
    """
    Обернул в класс методы которые возвращают timestamp
    Может вернуть дату + время , а может только время
    """
    def get_time_stamp(self) -> str:
        return datetime.datetime.today().strftime('%H:%M:%S')

    def get_datetime_stamp(self) -> str:
        return datetime.datetime.today().strftime('%c')


def get_var_list(plc)-> list: 
    try:
        symbols=plc.get_all_symbols()
        variables = []

        for s in symbols:
            if s.name[0] != '.':
                variables.append(s.name)

        return variables
    except:
        print('He have an error while we read stuff')


def get_vars_from_plc(plc,var_list) -> list:
    return plc.read_list_by_name(var_list)



