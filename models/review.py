#!/usr/bin/python3
"""This module creates a class for a review"""

from models.base import BaseModel


class Review(BaseModel):
    """A class on review information"""
    place_id = ""
    user_id = ""
    text = ""
