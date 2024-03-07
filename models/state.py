#!/usr/bin/python3
  "definig the class state"
  "every state will be identified by a unique name"

from models.base_model import BaseModel


class State(BaseModel):
    
    name = ""
