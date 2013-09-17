import unittest
from Bowling import Bowling     
    
class BowlingTests(unittest.TestCase):
    def testAllStrike(self):
        self.assertEqual(300, Bowling("XXXXXXXXXXXX").score())
    
    def testAllZero(self):
        self.assertEqual(0, Bowling("--------------------").score())
        
    def testAllSpare(self):
        self.assertEqual(150, Bowling("5/5/5/5/5/5/5/5/5/5/5").score())
        
    def testMixture(self):
        self.assertEqual(120, Bowling("X--X-/X--X-5XX-/").score())

if __name__ == '__main__':
    unittest.main()
