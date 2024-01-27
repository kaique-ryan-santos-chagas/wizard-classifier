import json, os

from playsound import playsound
from gtts import gTTS
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

print('Quantidade de neurônios:', len(inputs))
print('Quantidade de pesos:', len(weights_generated))

with open('model.json', 'w') as file:
    file.write(json.dumps(trained_model))


input = [1, 1, 0, 1, 0, 0, 0, 1, 1]

CORRECT_OUTPUT = 1

for weights in trained_model:
  
  sum = 0
  list_index = trained_model.index(weights)
  
  for weight in weights:
    index = weights.index(weight)
    sum = sum + input[index] * weight

  
  error = CORRECT_OUTPUT - sum

  if round(error, 1) == 0:
    if character_data[list_index]['Classe'] == 1:
      talk = 'Acho que você viu a bruxa ' + character_data[list_index]['Nome']
      tts = gTTS(talk, lang='pt')
      tts.save('ai_talk.mp3')
      playsound('ai_talk.mp3')
      os.unlink(os.getcwd() + '/ai_talk.mp3')
        
    elif character_data[list_index]['Classe'] == 0:
      talk = 'Acho que você viu o bruxo ' + character_data[list_index]['Nome']
      tts = gTTS(talk, lang='pt')
      tts.save('ai_talk.mp3')
      playsound('ai_talk.mp3')
      os.unlink(os.getcwd() + '/ai_talk.mp3')
        

