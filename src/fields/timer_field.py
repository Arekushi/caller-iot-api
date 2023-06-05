from datetime import datetime
from flask_restx import fields


class TimeField(fields.String):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def output(self, key, obj, ordered):
        value = None
        
        try:
            value = getattr(obj, key)
        except AttributeError:
            try:
                value = obj[key]
            except TypeError:
                return value
        
        if value is not None and isinstance(value, datetime):
            return value.strftime("%H:%M:%S")
        
        return value

    def parse(self, value):
        try:
            return datetime.strptime(value, "%H:%M:%S").time()
        except ValueError:
            raise ValueError("Invalid time format. Expected 'HH:MM:SS'.")
