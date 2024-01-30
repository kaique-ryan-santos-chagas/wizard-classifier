import random


class GenerateWeights:

    def __init__(self):

        self.weights_list = []


    def generate_weights(self, character_data):

        for data in character_data:
            weights = []
            for column in data:
                if column != 'Nome':
                    weight = random.uniform(0, 1)
                    weights.append(weight)

            self.weights_list.append(weights)

        return self.weights_list
