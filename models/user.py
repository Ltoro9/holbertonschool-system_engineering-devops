#!/usr/bin/python3
"""comment"""


from models.base_model import BaseModel


class User(BaseModel):
    '''
        User class
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
