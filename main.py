from typing import Union

from fastapi import FastAPI, Request, Path
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from functions.modelConfig import modelConfig, modelsList
from functions.importModel import importModel
from functions.transformers import transformersDict
import pandas as pd

app = FastAPI()

class ModelsBody(BaseModel):
    name: str = Field(..., example="0001_test")
    inputs:  Optional[List[Dict[str, Any]]] = Field(
        None,
        example=[
            {"const": 1, "Education": 12}
        ]
    )


@app.get("/")
def read_root():
    return "Hello Jason"

@app.get("/test")
def test(name: str , family: str):
    return f'{family} {name}'

@app.get("/models/list")
def models():
    return modelsList()

@app.get("/model/info/{modelName}")
def modelInfo(modelName: str = Path(..., example="0001_test")):
    return modelConfig(modelName)

@app.post("/model/predict")
def modelsInfo(body: ModelsBody):
    modelConfigGet = modelConfig(body.name)

    inputForPredict = []
    for indexBody, inputItemBody in enumerate(body.inputs or []):
        inputItemBodyPd = pd.Series(inputItemBody)
        transformers = modelConfigGet.get('transformers', [])
        for indexTransform, inputItemTransform in enumerate(transformers):
            transformer = transformers[indexTransform]
            inputItemBodyPd[transformer['name']] = transformersDict.get(transformer['transformer'])(inputItemBodyPd)
        inputForPredict.append(inputItemBodyPd)

    model = importModel({
        "modelName": modelConfigGet['name'],
        "baseRelativePath": ".",
    })

    result = model.predict(inputForPredict)

    return list(result)
