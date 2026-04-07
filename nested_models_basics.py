from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator , model_validator , computed_field
from typing import List , Dict , Optional , Annotated 

class Address(BaseModel):
    city : str
    state : str
    pin : int

class Patient(BaseModel):
    name : str
    age : int
    address : Address

address_details = {'city':'Jaipur','state':'Rajasthan','pin' : 302022}

address1 = Address(**address_details)

patient_details = {'name' : "Jacob",'age' : 50,'address' : address1}

patient1 = Patient(**patient_details)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)