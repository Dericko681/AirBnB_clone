#!/usr/bin/python3
 "Craeting the class user"
 

from models.base_model import BaseModel


class User(BaseModel):
 
    " Class user "
    email = ""
    password = ""
    firstName = ""
    lastName = ""
