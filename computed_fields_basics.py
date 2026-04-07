from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator , model_validator , computed_field
from typing import List , Dict , Optional , Annotated 

class Patient(BaseModel):
    name : str
    email : EmailStr
    linkedIn_url : AnyUrl
    age : int
    weight : float
    height : float
    married : bool = None
    allergies : List[str]
    contact_details : Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


def insert_patient_det(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print("BMI : ",patient.bmi)
    print("Inserted")

patient_info = {'name' : 'Aryan','email' : 'abcd@hdfc.com','linkedIn_url' : 'https://linkedin.com','age' : 30,'weight' : 75.00,'height' : 1.74,'allergies':['pollen','dust'],'contact_details' : {'Phone Number' : '1234567890'} }

patient1 = Patient(**patient_info)

insert_patient_det(patient1)