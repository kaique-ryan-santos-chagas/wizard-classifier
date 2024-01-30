import json

from prepare_data import PreparingData
from generate_weights import GenerateWeights
from get_inputs_from_data import GetInputsData
from activation_function import ActivationFunction
from train_model import TrainModel

preparing_data = PreparingData()
generating_weights = GenerateWeights()
getting_inputs = GetInputsData()
activating_neurons = ActivationFunction()

character_data = preparing_data.prepare_data()
weights_generated = generating_weights.generate_weights(character_data=character_data)
inputs = getting_inputs.get_inputs(character_data=character_data)
training_outputs = activating_neurons.active_neurons(inputs_list=inputs, weights_list=weights_generated)

training_model = TrainModel(weights_list=weights_generated, inputs_list=inputs, training_outputs=training_outputs)
trained_model = training_model.train()


with open('model.json', 'w') as file:
    file.write(json.dumps(trained_model))

        

