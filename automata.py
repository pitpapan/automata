import random
import numpy as np
import pandas as pd
import pickle


class Automaton:

    def __init__(self, number_of_states, alphabet):

        self.__NULL = 'O'  # Pythonic?
        self.number_of_states = number_of_states
        # TODO change 'O' initialization
        self.matrix = [[[] for y in range(number_of_states)]
                       for x in range(number_of_states)]
        self.states = np.array([f"q{y}" for y in range(number_of_states)])
        # maybe name _alphabet? pythonic?
        self.alphabet = alphabet
        self.initial_states = None
        self.final_states = []

    def redefine_states_names(self, names):
        if len(names) == len(self.states):
            self.states = np.array([y for y in names])
        else:
            raise ValueError(f"Error : {names} is not of the same size as the actuals states.")

    @staticmethod
    def random_moves_automaton(number_of_states, alphabet):

        rma = Automaton(number_of_states, alphabet)
        rma.matrix = np.array([[random.choice(alphabet) for y in range(
            number_of_states)] for x in range(number_of_states)])
        return rma

    def display_matrix(self):
        parapandas = np.array(self.matrix)

        return pd.DataFrame(
            data=parapandas,
            index=self.states,
            columns=self.states)
    # Check symbol name
    def is_on_alphabet(self, symbol):

        return symbol in self.alphabet
    # Add transition check if its on the dictonary

    def add_move(self, origin, destiny, transition):
        if self.is_on_alphabet(transition):
            self.matrix[origin][destiny].append(transition)
            #self.matrix[origin,destiny] = transition
        else:
            raise ValueError(f"Error : {transition} movement is not on the alphabet.")

    def delete_move(self, origin, destiny):

        self.matrix[origin, destiny] = self.__NULL

    def add_initial_state(self, initial_states):
        # TODO check if its inside the states
        # TODO check if its already one
        self.initial_states = initial_states

    def delete_initial_state(self, initial_states):

        self.initial_states = None

    def add_final_state(self, final_states):
        # TODO check if its inside the states
        # TODO fix problems with list and no list
        self.final_states.extend(final_states)

    def delete_final_state(self, final_states):

        self.final_states.remove(final_states)

    def moves_of_the_state(self, state):
        moves = []
        # TODO remove the else stament
        [moves.append(idx) if len(x) != 0 else '' for idx,
         x in enumerate(self.matrix[state])]
        return moves
        #return [idx if len(x) != 0 else None for idx,x in enumerate(self.matrix[state])]

        # return ([(self.states[x],moves[idx]) for idx,x in enumerate(moves)])

    def moves_to_the_state(self, state):
        moves = []
        # TODO remove the else stament
        [moves.append(idx) if len(self.matrix[idx][state]) != 0 else '' for idx in range(self.number_of_states)]

        return moves

    @staticmethod
    def load_automaton(path):

        return pickle.load(open(path, "rb"))


def create_automaton_two():
    A2 = Automaton(14, ['a', 'b'])
    A2.add_initial_state('q0')
    A2.add_final_state(['q7'])

    # q0 transition
    A2.add_move(0, 1, 'a')
    A2.add_move(0, 8, 'b')

    # q1 transition
    A2.add_move(1, 2, 'a')

    # q2 transition
    A2.add_move(2, 3, 'b')

    # q3 transition
    A2.add_move(3, 4, 'a')
    A2.add_move(3, 6, 'a')
    A2.add_move(3, 6, 'b')

    # q4 transition
    A2.add_move(4, 5, 'b')

    # q5 transition
    A2.add_move(5, 4, 'a')
    A2.add_move(5, 6, 'a')

    # q6 transition

    # q7 transition

    # q8 transition
    A2.add_move(8, 9, 'b')

    # q9 transition
    A2.add_move(9, 10, 'a')

    # q10 transition
    A2.add_move(10, 11, 'b')
    A2.add_move(10, 13, 'b')

    # q11 transition
    A2.add_move(11, 12, 'a')

    # q12 transition
    A2.add_move(12, 11, 'b')
    A2.add_move(12, 13, 'b')

    # q13 transition

    pickle.dump(A2, open("A2.p", "wb"))

    return A2


A2 = create_automaton_two()
array = A2.moves_to_the_state(2)
print(array)
