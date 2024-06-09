
import pickle

def importModel(config):
    
    baseRelativePath = config['baseRelativePath'] 
    modelName = config['modelName']
    with open(f'{baseRelativePath}/models/{modelName}','rb') as file:
        loaded_model = pickle.load(file)
    
    return loaded_model