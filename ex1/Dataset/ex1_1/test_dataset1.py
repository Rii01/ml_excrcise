import unittest
from dataset1 import true_function
import numpy as np

class Testdataset(unittest.TestCase):

    def test_true_function(self):
        self.assertEqual(0, true_function(0))

if __name__== "__main__":
    unittest.main()