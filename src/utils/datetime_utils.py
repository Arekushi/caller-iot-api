import datetime


def datetime_from_str(date:str, format='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.strptime(date, format)


def time_ms_diff(date_one, date_two):
    diff = datetime.datetime.combine(datetime.datetime.min, date_one.time()) - \
        datetime.datetime.combine(datetime.datetime.min, date_two.time())
        
    diff = diff.total_seconds() * 1000
    return diff
