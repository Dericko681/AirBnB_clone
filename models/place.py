#!/usr/bin/python3
"contains the code for the creation of the state class"
"every state will be idnetified by some attributes"
"the value of evry attribute is unique to evey state"


class Place(BaseModel):
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    
