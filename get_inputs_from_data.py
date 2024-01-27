

class GetInputsData:

    def __init__(self):

        self.inputs_list = []


    def get_inputs(self, character_data):

        for data in character_data:
            inputs = []
            for column in data:
                if column != 'Nome':
                    inputs.append(data[column])

            self.inputs_list.append(inputs)

        return self.inputs_list