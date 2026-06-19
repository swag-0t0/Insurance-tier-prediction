from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel,Field,field_validator,computed_field
from typing import List,Dict,Annotated,Literal,Optional
from Model.prediction import MODEL_VERSION,predict_output
from Schema.prediction_response import PredictionResponse
from Schema.user_input import UserInput

class Patient(BaseModel):
    id:Annotated[str,Field(...,description='Id of the patient',examples=['P001'])]
    name:Annotated[str,Field(...,description='Name of the patient')]
    city:Annotated[str,Field(...,description='Patients City')]
    age:Annotated[int,Field(...,gt=0,lt=120,description='Age of the patient')]
    gender:Annotated[Literal['male','Female','Other'],Field(...,description='Gender of Patient')]
    height:Annotated[float,Field(...,gt=0,description='Height of the patient')]
    weight:Annotated[float,Field(...,gt=0,description='Weight of the Patient')]

    @computed_field
    @property
    def bmi(self) ->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        bmi=self.bmi
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'   

class PatientUpdate(BaseModel):
    
    name:Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int],Field(default=None)]
    gender:Annotated[Optional[Literal['male','Female','Other']],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None)]
    weight:Annotated[Optional[float],Field(default=None)]


app = FastAPI()

@app.get('/')
def home():
    return {'message':'Welcome to Home!'}

@app.get('/health')
def health_check():
    return{'status':'device okay',
            'version':MODEL_VERSION,

    }

@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data:UserInput):

    user_input={
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'occupation':data.occupation
    }  

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200,content={'response':prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))      
