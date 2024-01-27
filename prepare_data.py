import json
import os

class PreparingData:

    def __init__(self):

        file_data_path = os.getcwd() + '/data/character_data.json'
        self.file_data_path = file_data_path.replace('/', '\\')

        character_data_file = open(self.file_data_path)
        self.character_data = json.load(character_data_file)

    def prepare_data(self):

        for column in self.character_data:
            if column['Habilidade Magica'] > 7:
                column['Habilidade Magica'] = 1
            else:
                column['Habilidade Magica'] = 0
            if column['Idade'] < 30:
                column['Idade'] = 1
            else:
                column['Idade'] = 0
            if column['Conhecimento de Pocoes'] > 7:
                column['Conhecimento de Pocoes'] = 1
            else:
                column['Conhecimento de Pocoes'] = 0
            if column['Astucia'] > 7:
                column['Astucia'] = 1
            else:
                column['Astucia'] = 0
            if column['Lealdade'] > 7:
                column['Lealdade'] = 1
            else:
                column['Lealdade'] = 0
            if column['Classe'] == 'Bruxa':
                column['Classe'] = 1
            else:
                column['Classe'] = 0
            if column['Animago'] == True:
                column['Animago'] = 1
            else:
                column['Animago'] = 0
            if column['Patrono'] == True:
                column['Patrono'] = 1
            else:
                column['Patrono'] = 0

            column['Bias'] = 1

        return self.character_data

