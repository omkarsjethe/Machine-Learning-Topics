from fastapi import FastAPI , Path , HTTPException , Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field
from typing import Annotated , Literal , Optional
import json

app= FastAPI()

class Patient(BaseModel):

    id : Annotated[str, Field(..., description='ID of the patient' , examples=['P001 '])]
    name : Annotated[str , Field(..., description='Name of the patient')]
     
    city : Annotated[str , Field(..., description='City where patient belongs')]
    age : Annotated[int , Field(..., gt=0 , lt=100, description='Age of the patient')]
    gender : Annotated[Literal['male' , 'female' ,'others'], Field(..., description='Gender of the patient')]
    height : Annotated[float ,Field(..., gt=0 , description='Height of the patient in mtrs')]
    weight : Annotated[float ,Field(..., gt=0 , description='Weight of the patient in Kg')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi< 25 : 
            return 'normal'
        elif self.bmi < 30 :
            return 'Overweight'
        else:
            return 'Obese'
        

class patientUpdate(BaseModel):
    name: Annotated[Optional[str],Field(default=None)]
    city : Annotated[Optional[str], Field(default=None)]
    age : Annotated[Optional[int],Field(gt=0 ,lt=120 , default=None)]
    gender : Annotated[Optional[Literal['male','female']], Field(default=None)]
    height : Annotated[Optional[float] , Field(gt=0 , default=None)]
    weight : Annotated[Optional[float] , Field(gt=0 , default=None)]
        

# utility function to load all the data from the database
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data

# utility fun to save the dictionary file into json format i.e. ,  the new data to the database
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.get("/")
def hello():
    return {'message':"Patient managament api system"}


@app.get("/about")
def about():
    return {'message':'A fully fucntional api which manage your patient records'}


@app.get("/view")
def view():
    data=load_data()
    return  data


@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(..., description='ID of the patient in the DB', example='P001')):
    # load all the data
    data = load_data()
    if patient_id in data: 
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail='Patient  not found')
    
    

@app.get("/sort")
def sort_patients(sort_by : str = Query(..., description='sort on the basis of height, weight, bmi') , order : str = Query('asc', description='order by asc or desc') ):
    valid_feilds = ['height' , 'weight' , 'bmi']

    if sort_by not in valid_feilds:
        raise HTTPException(status_code=400 ,  detail='invalid field select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400 , detail='invalid order select from asc of desc')
    
    data = load_data()
    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values() , key=lambda x: x.get(sort_by,0) , reverse=sort_order) 
    return sorted_data


@app.post('/create')
def create_patient(patient: Patient):

    # load existing data
    data = load_data()

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message':'patient created successfully'})



# Update code
@app.put("/edit{patient_id}")
def update_patient(patient_id : str , patient_update : patientUpdate):

    # load the data
    data = load_data()
    
    # check the patient_id is present or not
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient id is not present')
    
    # extract the data of the patient
    exsiting_patient_info = data[patient_id]
     
    # modify the fields which are sent by the user
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key , value in updated_patient_info.items():
        exsiting_patient_info[key]=value

    # existing_patient_info --> pydantic_object --> update_bmi + verdict
    exsiting_patient_info['id']=patient_id
    patient_pydantic_obj  = Patient(**exsiting_patient_info)
    # pydantic_obj --> dict
    exsiting_patient_info = patient_pydantic_obj.model_dump(exclude='id')

    # add this dictionary to data
    data[patient_id]= exsiting_patient_info

    # save the data
    save_data(data)

    return JSONResponse(status_code=200, content={'message': "Content updated"})



# Delete code
@app.delete("/delete/{patient_id}")
def delete_patient(patient_id : str):
    data =  load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404 , detail="Patient not found")
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200 , content={'message':"Patient deleted successfully"})


