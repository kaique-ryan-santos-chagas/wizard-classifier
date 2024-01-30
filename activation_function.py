
# Activation Function to active neurons in the network.

class ActivationFunction:

    def __init__(self):

        self.training_outputs = []
        self.CORRECT_OUTPUT = 1

    def active_neurons(self, inputs_list, weights_list):

        self.training_outputs.clear()

        for weights in weights_list:
            
            list_index = weights_list.index(weights)
            sum = 0
            
            for weight in weights:
                index = weights.index(weight)
                sum = sum + inputs_list[list_index][index] * weight

            error = self.CORRECT_OUTPUT - sum
            self.training_outputs.append(round(error, 1))

        print('Erros no treinamento:', self.training_outputs)
        return self.training_outputs