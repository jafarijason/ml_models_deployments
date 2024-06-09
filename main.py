from typing import Union

from fastapi import FastAPI, Request, Path
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from functions.modelConfig import modelConfig, modelsList
from functions.importModel import importModel

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
     # Iterate over each input item
    for indexBody, inputItemBody in enumerate(body.inputs or []):
        inputItem = []
        for indexConfig, inputItemConfig in enumerate(modelConfigGet['inputs'] or []):
            configValue = inputItemBody[inputItemConfig['name']]

            inputItem.append(configValue)
        inputForPredict.append(inputItem)

    model = importModel({
        "modelName": modelConfigGet['name'],
        "baseRelativePath": ".",
    })

    result = model.predict(inputForPredict)

    return list(result)
