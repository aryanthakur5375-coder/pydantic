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

temp = patient1.model_dump()
print(temp)
print(type(temp))

temp1 = patient1.model_dump(include = ['name','age'])
print(temp1)
print(type(temp1))

temp2 = patient1.model_dump(exclude = ['name','age'])
print(temp2)
print(type(temp2))

temp3 = patient1.model_dump_json()
print(temp3)
print(type(temp3))