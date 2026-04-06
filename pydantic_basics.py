from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List , Dict , Optional , Annotated 
class Patient(BaseModel):
    name : Annotated[str , Field(max_length = 50,Title = 'Name of the Patient',description = 'Name of the patient should be less than 50',exmaples = ['Aryan'])]    
    email : EmailStr
    linkedIn_url : AnyUrl
    age : int = Field(gt = 0 , lt = 120)
    weight : Annotated[float,Field(gt = 0,strict = True)]
    married : Annotated[bool, Field(default = None,description = 'Is the patient married or not?')]
    allergies : Annotated[Optional[List[str]], Field(default = None, max_length = 5)]
    contact_details : Dict[str,str]

def insert_patient_det(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print("Inserted")

patient_info = {'name' : 'Aryan','email' : 'abcd@gmail.com','linkedIn_url' : 'https://linkedin.com','age' : 30,'weight' : 75.00,'allergies':['pollen','dust'],'contact_details' : {'Phone Number' : '1234567890'} }

patient1 = Patient(**patient_info)

insert_patient_det(patient1)