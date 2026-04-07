from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator , model_validator
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

    @model_validator(mode = 'after')
    def validate_model_validator(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
                raise ValueError("Patients older than 60 must have an emegency number")
        return model

def insert_patient_det(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print("Inserted")

patient_info = {'name' : 'Aryan','email' : 'abcd@hdfc.com','linkedIn_url' : 'https://linkedin.com','age' : 30,'weight' : 75.00,'allergies':['pollen','dust'],'contact_details' : {'Phone Number' : '1234567890'} }

patient1 = Patient(**patient_info)

insert_patient_det(patient1)