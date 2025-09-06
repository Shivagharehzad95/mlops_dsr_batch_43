import torch
import io
###this adds type hints and checking to our data
from pydantic import BaseModel # this has nothing to do with ML models 
# BaseModel is just the parent class for everything that is strictly typed in Pydantic
from fastapi import FastAPI, Depends, UploadFile, File
from torchvision.models import ResNet
from PIL import Image
from torchvision.transforms import v2 as transforms
import torch.nn.functional as F


##This is the data model that describe the output of the API
class Result(BaseModel):
    catgory: str
    confidence: float

###create fastAPI instance
app = FastAPI()

##debug the massage to check that the app is runing
@app.get('/')
def read_roo():
    return{"massage": "API is runing. Visit /docs for the Swagger API documentation"}