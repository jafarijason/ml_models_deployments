import pickle
import json

def exportModel(config):
    baseRelativePath = config['baseRelativePath']
    with open(f'{baseRelativePath}/models/configs.json',"r") as file:
        modelsConfig = json.load(file)
    modelName = config['modelName']
    modelsConfig[modelName] = {}
    modelsConfig[modelName]['name'] = modelName
    model = config['model']
    inputs = config['inputs']
    output = config['output']
    description = config['description']
    modelsConfig[modelName]['inputs'] = inputs
    modelsConfig[modelName]['output'] = output
    modelsConfig[modelName]['description'] = description
    filename = f'{baseRelativePath}/models/{modelName}'
    pickle.dump(model, open(filename, 'wb'))
    with open(f'{baseRelativePath}/models/configs.json', "w") as outputFile:
        json.dump(modelsConfig, outputFile, indent = 4)

    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model