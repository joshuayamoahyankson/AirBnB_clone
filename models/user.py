#!/usr/bin/python3
"""This module creates a class for a user"""

from models.base import BaseModel


class User(BaseModel):
    """A class on users information"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
