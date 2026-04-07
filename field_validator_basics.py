from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator
from typing import List , Dict , Optional , Annotated 

class Patient(BaseModel):
    name : str
    email : EmailStr
    linkedIn_url : AnyUrl
    age : int
    weight : float
    married : bool = None
    allergies : List[str]
    contact_details : Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com','icici.com']

        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid name")
        return value
    
    @field_validator("name")
    @classmethod
    def upper_case(cls , value):
        return value.upper()

def insert_patient_det(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print("Inserted")

patient_info = {'name' : 'Aryan','email' : 'abcd@hdfc.com','linkedIn_url' : 'https://linkedin.com','age' : 30,'weight' : 75.00,'allergies':['pollen','dust'],'contact_details' : {'Phone Number' : '1234567890'} }

patient1 = Patient(**patient_info)

insert_patient_det(patient1)