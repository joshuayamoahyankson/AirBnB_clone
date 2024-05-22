#!/usr/bin/python3
"""This module creates a class for a city"""

from models.base import BaseModel


class City(BaseModel):
    """Class for controlling city objects"""
    state_id = ""
    name = ""
