#!/usr/bin/python3

from datetime import datetime
from models import storage
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs is not None and kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now
        if not kwargs:
            storage.new(self)

    def __str__(self):
        return (f"{self.__class__.__name__}, {self.id}, {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        emp_dict = dict()
        for key, value in self.__dict__.items():
            if value is not None:
                if key in ['created_at', 'updated_at']:
                    emp_dict[key] = value.isoformat()
                else:
                    emp_dict[key] = value
        emp_dict['__class__'] = self.__class__.__name__
        return emp_dict
