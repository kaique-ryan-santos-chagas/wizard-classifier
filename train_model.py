from activation_function import ActivationFunction

class TrainModel:

    def __init__(self, weights_list, inputs_list, training_outputs):

        self.training_outputs = training_outputs
        self.COEFFICIENT_LEARNING = 0.1
        self.weights_list = weights_list
        self.inputs_list = inputs_list
        self.activation_function = ActivationFunction()

    
    def backpropagation(self, training_outputs):

        for weights in self.weights_list:

            list_index = self.weights_list.index(weights)

            for weight in weights:
                
                index = weights.index(weight)
                new_weight = weight + self.COEFFICIENT_LEARNING * training_outputs[list_index] * self.inputs_list[list_index][index]
                print('Novo peso =', weight, '+', self.COEFFICIENT_LEARNING, '*', training_outputs[list_index], '*', self.inputs_list[list_index][index], '=', new_weight)
                weights[index] = new_weight

    
    def train(self):

        errors_verify = all(output == 0 for output in self.training_outputs)

        while not errors_verify:
            
            self.backpropagation(training_outputs=self.training_outputs)
            self.training_outputs = self.activation_function.active_neurons(inputs_list=self.inputs_list, weights_list=self.weights_list)
            errors_verify = all(output == 0 for output in self.training_outputs)

        return self.weights_list
       
    