#!/usr/bin/python3

"""
This class contains optional Amenity details to be supplied
in addition to the basecs.

"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class contains all the additional Amenity details to be supplied

    Attributes:
        Fields:
            name:string - The Amenity name
    """
    name = ""
