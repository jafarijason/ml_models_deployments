from typing import Union

from fastapi import FastAPI, Request, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import pandas as pd

from mlModelSaver import MlModelSaver
mlModelSaverInstance = MlModelSaver({
    "baseRelativePath": ".",
    "modelsFolder": "models"
})


app = FastAPI()

class ModelsBody(BaseModel):
    name: str = Field(..., example="0001_test")
    inputs:  Optional[List[Dict[str, Any]]] = Field(
        None,
        example=[
            {"Temperature": 56, "Advertising": 15, "Discount": 25}
        ]
    )


@app.get("/")
def read_root():
    return "Hello Jason"

@app.get("/models/list")
def models():
    return mlModelSaverInstance.listOfModels()

@app.get("/model/info/{modelName}")
def modelInfo(modelName: str = Path(..., example="0001_test")):
    model = mlModelSaverInstance.getModel(modelName)

    response = model.mlModelSaverConfig
    return response



@app.post("/model/predict")
def modelsInfo(body: ModelsBody):
    model = mlModelSaverInstance.getModel(body.name)

    inputDf = pd.DataFrame(body.inputs)
    return model.mlModelSavePredict(
        inputDf,
        getattr(body, 'typeOfPredict', 'normal')
    )
