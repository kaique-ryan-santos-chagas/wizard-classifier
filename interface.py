import json, os

from prepare_data import PreparingData
from playsound import playsound
from gtts import gTTS

training_data = PreparingData()

model_path = os.getcwd() + '/model.json'
model_json = open(model_path.replace('/', '\\'))

trained_model = json.load(model_json)
character_data = training_data.prepare_data()

input = [1, 0, 1, 1, 0, 0, 1, 1, 1]

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