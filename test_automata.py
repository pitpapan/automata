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

    def test_state_accesible(self):
        self.assertTrue(EmptyAutomaton.state_accesible(1))
        self.assertTrue(EmptyAutomaton.state_accesible(2))
        self.assertTrue(EmptyAutomaton.state_accesible(3))
        self.assertTrue(EmptyAutomaton.state_accesible(4))
        self.assertTrue(EmptyAutomaton.state_accesible(5))
        self.assertTrue(EmptyAutomaton.state_accesible(6))
        
        self.assertFalse(EmptyAutomaton.state_accesible(6))
        
        self.assertTrue(EmptyAutomaton.state_accesible(8))
        self.assertTrue(EmptyAutomaton.state_accesible(9))
        self.assertTrue(EmptyAutomaton.state_accesible(10))
        self.assertTrue(EmptyAutomaton.state_accesible(11))
        self.assertTrue(EmptyAutomaton.state_accesible(12))
        self.assertTrue(EmptyAutomaton.state_accesible(13))
        
        #S:0,A:1,B:2,C:3,D:4,E:5,F:6
        self.assertTrue(InfiniteAutomaton.state_accesible(1))
        
        self.assertFalse(InfiniteAutomaton.state_accesible(2))
        
        self.assertTrue(InfiniteAutomaton.state_accesible(3))
        self.assertTrue(InfiniteAutomaton.state_accesible(4))
        self.assertTrue(InfiniteAutomaton.state_accesible(5))
        self.assertTrue(InfiniteAutomaton.state_accesible(6))
    
    def test_state_coaccesible(self):
        self.assertFalse(EmptyAutomaton.state_coaccesible(0))
        self.assertFalse(EmptyAutomaton.state_coaccesible(1))
        self.assertFalse(EmptyAutomaton.state_coaccesible(2))
        self.assertFalse(EmptyAutomaton.state_coaccesible(3))
        self.assertFalse(EmptyAutomaton.state_coaccesible(4))
        self.assertFalse(EmptyAutomaton.state_coaccesible(5))
        self.assertFalse(EmptyAutomaton.state_coaccesible(6))
        self.assertFalse(EmptyAutomaton.state_coaccesible(7))
        self.assertFalse(EmptyAutomaton.state_coaccesible(8))
        self.assertFalse(EmptyAutomaton.state_coaccesible(9))
        self.assertFalse(EmptyAutomaton.state_coaccesible(10))
        self.assertFalse(EmptyAutomaton.state_coaccesible(11))
        self.assertFalse(EmptyAutomaton.state_coaccesible(12))
        
        #S:0,A:1,B:2,C:3,D:4,E:5,F:6
        
        self.assertTrue(InfiniteAutomaton.state_coaccesible(0))

        self.assertFalse(InfiniteAutomaton.state_coaccesible(1))

        self.assertTrue(InfiniteAutomaton.state_coaccesible(2))

        self.assertFalse(InfiniteAutomaton.state_coaccesible(3))

        self.assertTrue(InfiniteAutomaton.state_coaccesible(4))
        self.assertTrue(InfiniteAutomaton.state_coaccesible(5))
        








if __name__ == "__main__":
    unittest.main()
