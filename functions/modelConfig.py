import json


def modelConfig(modelName):
    with open(f'./models/configs.json',"r") as file:
        modelsConfig = json.load(file)
    modelName = modelsConfig[modelName]
    return modelName

def modelsList():
    with open(f'./models/configs.json',"r") as file:
        modelsConfig = json.load(file)
    keys = modelsConfig.keys()
    return list(keys)