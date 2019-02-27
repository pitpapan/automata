from automata import Automaton
import unittest

InfiniteAutomaton = Automaton.load_automaton("A.p")
EmptyAutomaton = Automaton.load_automaton("A2.p")


class test(unittest.TestCase):
    def test_is_infinite(self):
        self.assertTrue(InfiniteAutomaton.is_infinite())
        self.assertFalse(EmptyAutomaton.is_infinite())

    def test_is_empty(self):
        self.assertTrue(InfiniteAutomaton.is_empty())
        self.assertFalse(InfiniteAutomaton.is_infinite())


if __name__ == "__main__":
    unittest.main()
